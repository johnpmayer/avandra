"""
Main application code for Avandra.
"""

import asyncio

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

async def run_avandra():
    """Main entry point for the avandra agent application."""
    # MCPApp will automatically look for mcp_agent.config.yaml in the current directory
    app = MCPApp(name="avandra")
    
    async with app.run() as avandra_app:
        context = avandra_app.context
        logger = avandra_app.logger

        logger.info("Avandra starting...")
        logger.info("Current config:", data=context.config.model_dump())
        
        # Create and run the main agent
        main_agent = Agent(
            name="avandra",
            instruction="""You are Avandra, a headless code and document editing agent.
            Your job is to assist with code and document editing tasks.""",
            server_names=["filesystem"],  # Add other servers as needed
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
                message="Print the contents of mcp_agent.config.yaml verbatim",
            )
            logger.info(f"mcp_agent.config.yaml contents: {result}")


if __name__ == "__main__":
    asyncio.run(run_avandra())
