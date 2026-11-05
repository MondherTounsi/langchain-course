
import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv
load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__=="__main__":
    main()
