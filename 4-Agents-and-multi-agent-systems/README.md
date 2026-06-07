# 4 — Agents & Multi-Agent Systems

Building autonomous AI agents that plan, use tools, and collaborate.

## Topics Covered

- Tool use and function calling (Anthropic + OpenAI)
- ReAct loop: Reason → Act → Observe
- Agent memory: in-context, external (vector store), episodic
- Planning patterns: chain-of-thought, tree-of-thought, MCTS
- Multi-agent patterns: orchestrator/subagent, peer-to-peer, debate
- Claude Agent SDK: custom agents, handoffs, shared memory
- Safety and guardrails: prompt injection, loop detection

## Projects

| Project | Description |
|---------|-------------|
| `web-research-agent` | ReAct agent that searches and summarises |
| `code-agent` | Agent that writes, runs, and debugs code |
| `multi-agent-pipeline` | Orchestrator spawning specialist subagents |

## Setup

```bash
pip install anthropic httpx duckduckgo-search
```
