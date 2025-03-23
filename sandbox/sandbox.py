#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anthropic",
#     "mcp-agent",
# ]
# ///

import asyncio

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.mcp.mcp_agent_client_session import MCPAgentClientSession
from mcp_agent.mcp.mcp_connection_manager import MCPConnectionManager
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM


app = MCPApp(name="sandbox")

async def example_usage():
    async with app.run() as hello_world_app:
        context = hello_world_app.context
        logger = hello_world_app.logger

        logger.info("Hello, world!")
        logger.info("Current config:", data=context.config.model_dump())

        connection_manager = MCPConnectionManager(context.server_registry)
        await connection_manager.__aenter__()

        try:
            filesystem_client = await connection_manager.get_server(
                server_name="filesystem", client_session_factory=MCPAgentClientSession
            )
            # result = await filesystem_client.list_tools()
            # logger.info("Filesystem Tools available:", data=result.model_dump())
            logger.info("filesystem: Connected to server with persistent connection.")

            # TODO figure out how to list the tools

            # TODO add the local python server
            
        finally:
            await connection_manager.disconnect_server(server_name="filesystem")
            logger.info("filesystem: Disconnected from server.")
        
        finder_agent = Agent(
            name="finder",
            instruction="""You are an agent with access to the filesystem, 
            as well as the ability to fetch URLs. Your job is to identify 
            the closest match to a user's request, make the appropriate tool calls, 
            and return the URI and CONTENTS of the closest match.""",
            server_names=["filesystem"],
        )

        async with finder_agent:
            logger.info("finder: Connected to server, calling list_tools...")
            result = await finder_agent.list_tools()
            tool_names = [tool["name"] for tool in result.model_dump()["tools"]]
            logger.info("Tools available:", data=tool_names)

            llm = await finder_agent.attach_llm(OpenAIAugmentedLLM)
            result = await llm.generate_str(
                message="Print the contents of mcp_agent.config.yaml verbatim",
            )
            logger.info(f"mcp_agent.config.yaml contents: {result}")

if __name__ == "__main__":
    asyncio.run(example_usage())