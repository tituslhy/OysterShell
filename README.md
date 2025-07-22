# OysterShell
How to host your LLM

We explore:
1. Ollama
2. Docker
3. vLLM

This GitHub repository is a companion resource to the medium article [Service please 👨🏻‍🍳 : 3 ways to serve an LLM](https://medium.com/@tituslhy/service-please-3-ways-to-serve-an-llm-ca5ead2547e6).

<p align="center">
    <img src="./images/eggs_served.webp">
</p>

## Setup

### General
This repository uses the [uv package installer](https://docs.astral.sh/uv/pip/packages/). 

To create a virtual environment with the dependencies installed, simply type in your terminal:
```
uv sync
```

### vLLM
To setup your vLLM, run the notebook `2a. setup_vllm.ipynb` on Google Colab with the T4 GPU runtime selected.

### Ollama
To setup Ollama, follow the instructions on [Ollama's setup website](https://ollama.com/download).
