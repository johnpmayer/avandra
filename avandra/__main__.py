"""
Entry point for running Avandra as a module.
Example: python -m avandra run task_file.txt
"""

import asyncio
import sys
import typer
from pathlib import Path
from .app import run_avandra

def main(task: Path):
    """Run the Avandra agent with the specified task file."""
    sys.exit(asyncio.run(run_avandra(task_file=task)))

if __name__ == "__main__":
    typer.run(main)
