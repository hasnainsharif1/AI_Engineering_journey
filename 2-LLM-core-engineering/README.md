# 2 — LLM Core Engineering

Deep dive into how large language models work and how to use them via API.

## Topics Covered

- Transformer architecture: attention, positional encoding, layer norm
- Tokenisation: BPE, WordPiece, SentencePiece
- Claude / OpenAI API: completions, streaming, tool use
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- Token counting, context windows, and cost estimation
- Structured outputs and JSON mode
- Model evaluation: BLEU, ROUGE, LLM-as-judge

## Projects

| Project | Description |
|---------|-------------|
| `token-counter` | Count tokens and estimate costs across models |
| `structured-extractor` | Extract typed data from unstructured text |
| `prompt-playground` | Compare prompt strategies side by side |

## Setup

```bash
pip install anthropic tiktoken python-dotenv
```

Add your API key to `.env`:

```
ANTHROPIC_API_KEY=sk-ant-...
```
