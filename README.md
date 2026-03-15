# 🤖 End-to-End ReAct AI Agent with Dynamic LLM Routing

### Developed by - AL NOOR ISTIAK MAHMUD

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

A production-ready, full-stack Artificial Intelligence application that utilizes **LangGraph** to create a ReAct (Reasoning and Acting) agent. This system features decoupled Client-Server architecture, dynamic LLM selection (Groq vs. OpenAI), and autonomous web searching capabilities via the Tavily API.

### 🔗 Live Demo

### 🔗 Live Demo

- **Frontend (Streamlit):** [https://noor-ai-agent.streamlit.app/](https://noor-ai-agent.streamlit.app/)
- **Backend API Docs (Swagger UI):** [https://ai-agent-backend-ocot.onrender.com/docs](https://ai-agent-backend-ocot.onrender.com/docs)

---

## 🏗️ System Architecture

This project follows a strict decoupled architecture, separating the UI layer from the AI processing engine.

<div align="center">
  <img src="./diagrams/architecture.png" alt="System Architecture" width="800">
</div>

## ✨ Key Features

- **Agentic Workflow:** Built with LangGraph, allowing the AI to logically reason through queries and decide when to use external tools.
- **Autonomous Web Search:** Integrated with Tavily Search API, enabling the LLM to fetch real-time data beyond its training cutoff.
- **Dynamic LLM Routing:** Users can seamlessly switch between open-source models (via Groq) and proprietary models (OpenAI) at runtime.
- **Strict Schema Validation:** Utilizes Pydantic to enforce data contracts between the Streamlit frontend and FastAPI backend, preventing payload errors.
- **Interactive UI:** A clean, user-friendly interface built with Streamlit, including loading states and dynamic dropdowns.

## 🛠️ Tech Stack

- **Frontend:** Streamlit, Requests
- **Backend:** FastAPI, Uvicorn, Pydantic
- **AI Framework:** LangChain, LangGraph
- **LLM Providers:** Groq (Llama-3.3-70b, Mixtral), OpenAI (GPT-4o-mini)
- **Tools:** Tavily Search API

## 🚀 Local Installation & Setup

Want to run this project on your local machine? Follow these steps:

**1. Clone the repository**

````bash
git clone [https://github.com/alnooristiak/AI-Agent-Chatbot](https://github.com/alnooristiak/AI-Agent-Chatbot)
cd AI-Agent-Chatbot


**2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/Scripts/activate  # For Windows (Git Bash)

````

**3. Install Dependencies**

```bash
pip install -r requirements.txt

```

**4. Set up Environment Variables**
Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

```

**5. Run the Backend Server**

```bash
python backend.py

```

> The API will be available at http://127.0.0.1:9999/docs

**6. Run the Frontend App**
Open a new terminal, activate the environment, and run:

```bash
streamlit run frontend.py

```

## 🔮 Future Scope

- **Memory Integration:** Implement `ConversationBufferMemory` to retain chat history context.
- **Custom Tools:** Add more tools like Wikipedia Search or Arxiv paper fetcher.
- **Dockerization:** Containerize the application using Docker for easier deployment.

If you found this project helpful, feel free to give it a ⭐!

```

© alnooristiak

```
