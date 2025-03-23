"""
Entry point for running Avandra as a module.
Example: python -m avandra
"""

import asyncio
import sys
from .app import run_avandra

if __name__ == "__main__":
    sys.exit(asyncio.run(run_avandra()))
