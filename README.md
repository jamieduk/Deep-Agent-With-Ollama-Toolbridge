# 🧠 Deep Agent CLI: Coding Assistant with Memory
A powerful **command-line interface (CLI)** combining the stateful, multi-agent capabilities of **Deep Agent** with **Toolbridge** for enhanced model compatibility.  
This creates a robust, memory-enabled coding and research assistant powered by **LangGraph** and **Ollama**.

---

## 🔑 Prerequisite: API Key Setup (Tavily)

This project requires a **search API key** to enable web-grounding and research functionality.

1. Obtain your API key from [Tavily AI](https://tavily.com).
2. The key must be set as an environment variable in your `start.sh` file.

**Example (`start.sh`):**
```bash
export TAVILY_API_KEY="tvly-dev-CHANGE-API-KEYE-HERE"
⚡ Quick Setup (Recommended)
If you have all prerequisites installed (Python 3.x, Ollama), the auto-setup script will handle environment creation and dependency installation:

bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull minimax-m2:cloud

./setup.sh
🛠️ Manual Setup
If you prefer more control, follow these steps to manually configure the environment.

1. Create and Activate Virtual Environment
bash
python -m venv venv
source venv/bin/activate
2. Install Required Libraries
bash
pip install deepagents tavily
pip install -U langchain-ollama
3. Start the Deep Agent CLI
Ensure your start.sh file includes your Tavily API key, then run:

bash
./start.sh
💻 Example Execution Output
The script activates the environment and initializes the LangGraph architecture:

bash
./start.sh
Virtual Environment Setup and ready!

LangGraph is a library for building stateful, multi-agent applications with Large Language Models (LLMs). It's part of the LangChain ecosystem and is designed to help developers create complex AI workflows that can:
...
(venv) jay@jnetai:~/Documents/Scripts/AI/Deep-Agent-Cli$
🧩 Core Features (Powered by LangGraph)
The Deep Agent framework leverages the following advanced capabilities:

State Management: Maintains context and state across multiple LLM calls or agent interactions.

Multi-Agent Workflows: Enables coordinated interaction between multiple specialized AI agents.

Graph-Based Architecture: Defines complex workflows, decision trees, and reasoning paths.

Human-in-the-Loop: Allows for human intervention and approval at various stages.

Persistence: Saves and resumes ongoing agent workflows.

Streaming: Supports real-time response streaming.

🌉 Toolbridge Integration
This combined project utilizes Toolbridge to enhance compatibility between models.

Toolbridge is required when using models that do not natively support tool calling (function/tool use).
It acts as an intermediary, allowing such models to interact with external tools and functions within the Deep Agent pipeline.

Read Notes.txt for more help in setting up ollama and getting the cloud model

Original Toolbridge Repository: Oct4Pie/toolbridge

🔗 Project Sources and Credits
This project builds upon several open-source initiatives:

Component	Repository Link	Original Project
Deep Agent with Ollama Toolbridge	https://github.com/jamieduk/Deep-Agent-With-Ollama-Toolbridge	-
Deep Agent	https://github.com/langchain-ai/deepagents	LangChain AI
Toolbridge	https://github.com/Oct4Pie/toolbridge	Oct4Pie
LangGraph Overview	YouTube Video: LangGraph Introduction	LangChain AI

