from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tavily_search = TavilySearch(
    max_results=5,
    topic="general",
)

llm = ChatOpenAI(model="gpt-5")
tools = [tavily_search]
agent = create_agent(model=llm, tools=tools, system_prompt="You are a helpful research assistant. Use web search to find accurate, up-to-date information.")

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()
