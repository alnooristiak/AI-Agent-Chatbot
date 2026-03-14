import os
from dotenv import load_dotenv
# llm and tools call
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# env
load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

# llm model calling
openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Search Engine Tool
search_tool=TavilySearchResults(max_results=2)

system_prompt="Act as an AI chatbot who is smart and friendly"

agent=create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt
)

query="Tell me about the trends in crypto markets present time and when relese new meme coins and there updated infos with company name resons"

state={"messages": query}
response=agent.invoke(state)
messages=response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])