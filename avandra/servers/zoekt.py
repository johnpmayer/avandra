"""
Zoekt search MCP server for Avandra.
"""

import subprocess
import json
import os
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP

# N.B. I don't know how well this tool self-documents its purpose and capabilities

mcp = FastMCP("Avandra Zoekt Search Server")

zoekt_git_index_command = os.path.expanduser("~/go/bin/zoekt-git-index")
zoekt_command = os.path.expanduser("~/go/bin/zoekt")

def run_indexing():
    """Run the zoekt-git-index command to index the repository."""
    try:
        # Ensure the .zoekt directory exists
        os.makedirs(".zoekt", exist_ok=True)
        
        # Run the indexing command
        result = subprocess.run(
            [zoekt_git_index_command, "-incremental=0", "-index", ".zoekt", "."],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result.stdout
    except Exception as e:
        return json.dumps({"error": str(e)})


# Run indexing when the server starts
print("Indexing repository with zoekt...")
indexing_result = run_indexing()
print(f"Indexing complete: {indexing_result}")

def run_zoekt_command(query: str) -> str:
    """Run the zoekt command line tool with the given query."""
    try:
        result = subprocess.run(
            [zoekt_command, "-index_dir", ".zoekt", query],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result.stdout
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool("search")
def search(query: str) -> str:
    """Search the zoekt index with the given query."""
    result = run_zoekt_command(query)
    return result


@mcp.tool("reindex")
def reindex_tool() -> Dict[str, Any]:
    """Trigger re-indexing of the repository."""
    print("Re-indexing repository with zoekt...")
    result = run_indexing()
    print(f"Re-indexing complete: {result}")
    return {"status": "complete", "result": result}


@mcp.tool("read-query-syntax-manual")
def get_query_syntax() -> str:
    """Return the zoekt query syntax documentation."""
    try:
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the query syntax file
        syntax_file_path = os.path.join(current_dir, "zoekt_query_syntax.md")
        
        with open(syntax_file_path, "r") as f:
            return f.read()
    except Exception as e:
        return json.dumps({"error": str(e)})


# @mcp.resource("config://zoekt")
# def get_config() -> str:
#     """Return configuration information about zoekt."""
#     return json.dumps({
#         "name": "Avandra Zoekt Search Server",
#         "index_dir": ".zoekt/",
#         "command_path": "~/go/bin/zoekt",
#         "index_command_path": "~/go/bin/zoekt-git-index"
#     })


def run_server():
    """Run the server when executed directly."""
    mcp.run(transport='stdio')


if __name__ == "__main__":
    run_server()
