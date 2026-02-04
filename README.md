LangGraph-Based Agentic Blog Generation Pipeline
📌 Overview

This project is an agentic AI-based blog generation system that creates structured blog titles and long-form content from user prompts using OpenAI LLMs. It supports controlled content generation through reusable prompt templates and automatic multilingual translation.

The system is orchestrated using LangGraph, enabling a multi-node workflow with state management and conditional routing. It incorporates LLM memory and context persistence to maintain coherence across content generation and translation stages. The workflow is observable and debuggable using LangSmith, and the application is exposed via a FastAPI backend for scalable integration.

Supported languages:

English

Hindi

French

🏗️ Architecture

LLMs: OpenAI

Workflow Orchestration: LangGraph

Observability: LangSmith

Backend API: FastAPI

Prompt Engineering: Reusable, structured templates

State & Memory: Context persistence across nodes

⚙️ Prerequisites

Python 3.10+

OpenAI API Key

(Optional) Groq API Key

Git

🔐 Environment Setup

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=agentic-blog-generation


⚠️ Do not commit .env to GitHub.

📦 Installation

Clone the repository:

git clone https://github.com/sheetalmathur/LangGraph-Based-Agentic-Blog-Generation-Pipeline.git
cd LangGraph-Based-Agentic-Blog-Generation-Pipeline


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

▶️ Run the Application

Start the FastAPI application using app.py:

python app.py


Once running, the API will be available at:

http://localhost:8000


Swagger UI:

http://localhost:8000/docs
