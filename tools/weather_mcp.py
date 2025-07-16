
"""
This code will automatically generate a FastMCP server that will

- Use the agent workflow class name as the tool name
- Use our custom RunEvent as the typed inputs to the tool
- Automatically use the SSE stream for streaming json dumps of the workflow event stream
"""

from llama_index.core.agent.workflow import AgentStream, FunctionAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai_like import OpenAILike
from llama_index.tools.mcp.utils import workflow_as_mcp


docker_url = "http://localhost:12434/engines/v1"
docker_llm = "ai/deepseek-r1-distill-llama:8B-Q4_K_M"

llm = OpenAILike(
    model = docker_llm,
    api_base = docker_url,
    api_key = "fake",
    is_chat_model = True,
    is_function_calling_model = True,
    temperature = 0
)
def get_weather(location: str) -> str:
    """Use this tool to get the weather in a location."""
    return f"The weather in {location} is sunny."

weather_agent = FunctionAgent(
    llm = llm,
    name = "weather_agent",
    description = "An agent that can answer questions about the weather.",
    tools = [FunctionTool.from_defaults(get_weather)]
)

mcp = workflow_as_mcp(
    weather_agent,
    workflow_name = 'weather_agent', 
    workflow_description = 'An agent that can answer questions about the weather.',
    port=8000
)

if __name__ == "__main__":
    mcp.run(transport="sse")
