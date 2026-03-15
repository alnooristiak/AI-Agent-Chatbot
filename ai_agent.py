import os
from dotenv import load_dotenv
# LLM and Tools calls
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

from langchain_core.messages import AIMessage, HumanMessage 

# Load environment variables
load_dotenv()

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, groq_api_key=os.environ.get("GROQ_API_KEY"))
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, openai_api_key=os.environ.get("OPENAI_API_KEY"))
    else:
        return "Invalid Provider Selected"

    # Search Engine Tool Setup
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    
    # Create ReAct Agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    
    
    state = {"messages": [HumanMessage(content=query)]}
    
    try:
        response = agent.invoke(state)
        messages = response.get("messages", [])
        

        for message in reversed(messages):
            if isinstance(message, AIMessage) and message.content:
                return message.content
        
        return "No clear response found."
        
    except Exception as e:
        return f"Agent Error: {str(e)}"