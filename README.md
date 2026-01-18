# AI Agent with Calculator Tool

An interactive AI agent that can perform calculations and have conversations using the ReAct (Reasoning + Acting) framework.

## Overview

This project uses LangChain and LangGraph modules. The agent can:
- Process user queries and decide when to use available tools
- Perform calculations using a built-in calculator tool
- Respond naturally to general chat messages

## Requirements

- Python 3.12 or higher
- OpenAI API key

## Installation

1. Install dependencies using `uv`:
```bash
uv sync
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the agent with:
```bash
uv run main.py
```

Start chatting with the agent. You can ask it to perform calculations or just chat with it. Type `quit` to exit.

### Example Interactions

- "What is 5 plus 10?"
- "Calculate 100 divided by 4"
- "Tell me a joke"

## Dependencies

- **langchain** - Framework for building AI applications
- **langchain-openai** - OpenAI integration for LangChain
- **langgraph** - Framework for building AI agents with graphs
- **python-dotenv** - Loads environment variables from `.env` file

## Architecture

The agent uses the ReAct pattern:
1. **Reasoning**: The AI model analyzes the user input
2. **Acting**: If needed, it calls appropriate tools (like the calculator)
3. **Observing**: It processes the tool results and generates a response

The calculator tool is available for basic arithmetic operations.
