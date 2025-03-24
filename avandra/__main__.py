"""
Entry point for running Avandra as a module.
Example: python -m avandra run task_file.txt
"""

import asyncio
import sys
import typer
from pathlib import Path
from .app import run_avandra

def main(
    task: Path, 
    system_prompt_file: Path = None
):
    """Run the Avandra agent with the specified task file.
    
    Args:
        task: Path to the task file
        system_prompt_file: Optional path to a file containing custom system prompt
                         to override default instructions
    """
    sys.exit(asyncio.run(run_avandra(task_file=task, system_prompt_file=system_prompt_file)))

if __name__ == "__main__":
    typer.run(main)
