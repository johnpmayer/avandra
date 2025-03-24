"""
Main application code for Avandra.
"""

import asyncio
from pathlib import Path
from typing import Optional

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

async def run_avandra(task_file: Path, system_prompt_file: Optional[Path] = None):
    """Main entry point for the avandra agent application."""
    # MCPApp will automatically look for mcp_agent.config.yaml in the current directory
    app = MCPApp(name="avandra")

    async with app.run() as avandra_app:
        context = avandra_app.context
        logger = avandra_app.logger

        logger.info("Avandra starting...")
        logger.info("Current config:", data=context.config.model_dump())

        # Use the task file contents as the initial message
        try:
            with open(task_file, 'r') as f:
                task_content = f.read()
            
            logger.info(f"Using task from file: {task_file}")
        except Exception as e:
            logger.error(f"Error reading task file: {e}")
            raise

        if system_prompt_file:
            try:
                instruction = system_prompt_file.read_text()
                logger.info(f"Using system prompt from file: {system_prompt_file}")
            except Exception as e:
                logger.error(f"Error reading system prompt file: {e}")
                raise
        else:
            instruction = """You are Avandra, a headless code and document editing agent.
            Your job is to assist with code and document editing tasks."""

        # Create and run the main agent
        main_agent = Agent(
            name="avandra",
            instruction=instruction,
            server_names=["filesystem", "zoekt"],  # Add other servers as needed
        )

        async with main_agent:
            logger.info("Avandra agent initialized")
            # Main agent logic would go here
            
            # Example: List available tools
            result = await main_agent.list_tools()
            tool_names = [tool["name"] for tool in result.model_dump()["tools"]]
            logger.info("Tools available:", data=tool_names)
            
            # Example: Attach LLM
            llm = await main_agent.attach_llm(OpenAIAugmentedLLM)

            result = await llm.generate_str(
                message=task_content,
            )
            logger.info(f"Task result: {result}")
