#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "mcp-agent",
# ]
# ///

import asyncio

from mcp_agent.app import MCPApp
from mcp_agent.mcp.mcp_agent_client_session import MCPAgentClientSession
from mcp_agent.mcp.mcp_connection_manager import MCPConnectionManager

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

if __name__ == "__main__":
    asyncio.run(example_usage())