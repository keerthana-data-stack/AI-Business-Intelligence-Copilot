import streamlit as st
from backend.copilot import process_question

def render_ai_assistant(
        df,
        summary,
        quality,
        correlations
    ):

    st.header("🤖 AI Assistant")

    st.write(
        "Ask questions about your dataset in natural language."
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Ask a question about your data...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        answer = process_question(
            df,
            prompt,
            summary,
            quality,
            correlations
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )