"""
Example MCP server for Avandra.
"""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Avandra Hello Server")


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "Avandra configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"


def run_server():
    """Run the server when executed directly."""
    mcp.run(transport='stdio')


if __name__ == "__main__":
    run_server()
