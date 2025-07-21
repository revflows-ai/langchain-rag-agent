# LangChain Documentation Helper

A conversational assistant for querying LangChain documentation using natural language. Built with Streamlit, LangChain, Pinecone, and OpenAI.

## Features
- **Conversational UI:** Ask questions about LangChain and get answers with cited sources.
- **Retrieval-Augmented Generation (RAG):** Uses vector search over official documentation.
- **History-Aware:** Remembers chat context for better answers.
- **Easy Ingestion:** Scripts to load and index docs from local HTML files.
- **Demo Notebooks:** Explore Tavily's web crawling and extraction tools.

## Project Structure
- `main.py` — Streamlit app for the chat interface.
- `backend/core.py` — Core logic for LLM-powered retrieval and answer generation.
- `ingestion.py` — Script to ingest and index documentation into Pinecone.
- `logger.py` — Utility for colored terminal logging.
- `langchain-docs/` — Downloaded LangChain documentation (HTML, used as knowledge base).
- `Tavily Crawl Demo Tutorial.ipynb` / `Tavily Demo Tutorial.ipynb` — Jupyter notebooks for Tavily web crawling/extraction demos.
- `Pipfile` / `Pipfile.lock` — Python dependencies.

## Setup
1. **Install dependencies:**
   ```bash
   pipenv install
   # or
   pip install -r requirements.txt  # if you convert Pipfile to requirements.txt
   ```
2. **Set environment variables:**
   - Create a `.env` file with your OpenAI and Pinecone API keys (and Tavily API key for notebooks):
     ```env
     OPENAI_API_KEY=your-openai-key
     PINECONE_API_KEY=your-pinecone-key
     TAVILY_API_KEY=your-tavily-key  # (optional, for notebooks)
     ```
3. **Ingest documentation:**
   ```bash
   python ingestion.py
   ```
   This loads and indexes the docs into Pinecone.
4. **Run the app:**
   ```bash
   streamlit run main.py
   ```

## Usage
- Open the Streamlit app in your browser.
- Enter questions about LangChain. The bot will answer and cite documentation sources.

## Notebooks
- `Tavily Crawl Demo Tutorial.ipynb` and `Tavily Demo Tutorial.ipynb` show how to use Tavily's tools for intelligent web crawling and content extraction. See notebook cells for setup and usage.

## Requirements
- Python 3.13+
- See `Pipfile` for all dependencies (LangChain, Streamlit, Pinecone, OpenAI, etc.)

## License
See [LICENSE](LICENSE).# langchain-rag-agent
