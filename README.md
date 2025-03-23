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