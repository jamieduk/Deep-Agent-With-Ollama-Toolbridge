#
# (c) J~Net 2025
#
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
# 1. Import the LangChain Ollama model
from langchain_community.chat_models import ChatOllama


# --- CONFIGURATION START ---

# 2. Define your desired Ollama model name
# Example: "llama3", "mistral", or "qwen2"
OLLAMA_MODEL_NAME="minimax-m2:cloud" # minimax-m2:cloud

# Tavily client setup (still needed for the internet search tool)
tavily_client=TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# --- CONFIGURATION END ---


# Web search tool (remains the same)
def internet_search(
    query: str,
    max_results: int=5,
    topic: Literal["general", "news", "finance"]="general",
    include_raw_content: bool=False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# System prompt (remains the same)
research_instructions="""You are an expert researcher. Your job is to conduct thorough research, and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

# 3. Initialize the Ollama model object
ollama_model=ChatOllama(model=OLLAMA_MODEL_NAME)

# 4. Create the deep agent, passing the Ollama model
agent=create_deep_agent(
    model=ollama_model,  # <-- Pass the initialized model here
    tools=[internet_search],
    system_prompt=research_instructions,
)

# Invoke the agent (remains the same)
result=agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

print(result["messages"][-1].content)
