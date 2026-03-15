from dotenv import load_dotenv
load_dotenv()


# Setup UI with streamlit
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")


# text input area
system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

# model info
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# provider checkbok 
provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)
    
# websearch
allow_web_search=st.checkbox("Allow Web Search")

# user query
user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

# aipi path fastapi
API_URL="https://ai-agent-backend-ocot.onrender.com/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        # Prepare the payload
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        # Show a loading spinner while waiting for the response
        with st.spinner("Thinking... Please wait (Initial request may take up to 1 minute on Render Free Tier)"):
            try:
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    if isinstance(response_data, dict) and "error" in response_data:
                        st.error(response_data["error"])
                    else:
                        st.subheader("Agent Response")
                        
                        st.markdown(response_data)
                else:
                    st.error(f"Backend Error: Status Code {response.status_code}")
                    st.info("The server might be waking up. Please try again in 30 seconds.")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a query before clicking the button.")

# Footer
st.divider()
st.caption("Developed by Al Noor Istiak Mahmud | Powered by LangGraph & FastAPI")