from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """
    Schema for a source used by agents
    """

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """
    Schema for agent response with answer and sources
    """

    answer:str = Field(description="The agent's answer for the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


tavily_search = TavilySearch(
    max_results=5,
    topic="general",
)
llm = ChatOpenAI(model="gpt-5")
tools = [tavily_search]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()
