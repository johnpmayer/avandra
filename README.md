# Avandra

Automated
Virtual
Agent;
Navigating,
Diagnosing,
Reflecting,
Authoring

(It's also a deity in DnD, also known as "The Changebringer")

## Goals

`avandra` is a **headless** code and document editing agent.

The aspirational deployment model is to deploy avandra in some environment where they
can check out a repository, request a task from a work queue, and make edits in the
repository.

## Installation

### Using pip

(Not yet published...)

### Development Installation

```bash
# Install in development mode
pip install -e .
# If using a virtual environment
source ${VENV}/bin/activate
uv pip install -e .
```

## Usage

### Running Avandra

```bash
# Run the main application
python -m avandra

# Run a specific server
python -m avandra.servers.hello
```

### Configuration

Avandra uses `mcp_agent.config.yaml` in the current working directory for configuration.

## Ideas

* FSM; agent can automatically switches between modes (e.g. PLAN/ACT)
* Support cost tracking; a task can "eject" when it goes over budget
* MCP
* "Intra-Task Context Stack" to reduce context window when sub-milestones are deemed completed
* Task history export

## Tech Stack

* python
* uv
* langchain?
