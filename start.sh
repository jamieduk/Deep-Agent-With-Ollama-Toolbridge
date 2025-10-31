#!/bin/bash
# (c) J~Net 2025
#
export TAVILY_API_KEY="tvly-dev-f--CHANGE-APIKEY-HERE"
#
python -m venv venv
source venv/bin/activate
echo "Virtual Environment Setup and ready!"

python ollama-proxy-run.py # using the toolbridge proxy for ollama models that cantnormally use tools
#python ollama-run.py # for ollama models that can use tools
#python run.py # using tavily online paid api access
