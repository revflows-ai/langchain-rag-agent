import streamlit as st
from typing import Optional, Iterable
from backend.core import run_llm
import datetime

st.header("Langchain Udemy Course Documentation Helper Bot")

# Sidebar with user information (static for demo)
with st.sidebar:
    st.image("https://randomuser.me/api/portraits/men/75.jpg", width=100)
    st.markdown("**Name:** John Doe")
    st.markdown("**Email:** johndoe@example.com")

# Robust session state initialization
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# --- Chat UI Upgrade ---
# Display chat history
if (
    isinstance(st.session_state["chat_answers_history"], list)
    and isinstance(st.session_state["user_prompt_history"], list)
    and st.session_state["chat_answers_history"]
):
    for generated_response, user_query in zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"]):
        with st.chat_message("user", avatar="🧑"):
            st.write(user_query)
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(generated_response, unsafe_allow_html=True)

# Chat input at the bottom
user_prompt = st.chat_input("Enter your prompt here...")

# Helper for sources

def create_sources_string(source_urls: Optional[Iterable[str]]) -> str:
    if not source_urls or not isinstance(source_urls, (set, list)):
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string

if user_prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            query=user_prompt,
            chat_history=st.session_state["chat_history"]
        )
        source_docs = generated_response.get("source_documents")
        sources = set([doc.metadata["source"] for doc in source_docs]) if source_docs else set()

        formatted_response = (
            f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(user_prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", user_prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))

        # Display the new messages immediately
        with st.chat_message("user", avatar="🧑"):
            st.write(user_prompt)
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(formatted_response, unsafe_allow_html=True)

