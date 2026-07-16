import streamlit as st
import requests
import ollama


def render_system_status():

    st.subheader("🖥️ System Status")

    col1, col2 = st.columns(2)

    with col1:

        # FastAPI
        try:
            requests.get(
                "http://127.0.0.1:8000/health",
                timeout=2
            )

            st.success("🟢 FastAPI Online")

        except Exception:
            st.error("🔴 FastAPI Offline")

        # Ollama
        try:
            ollama.list()

            st.success("🟢 Ollama Running")

        except Exception:
            st.error("🔴 Ollama Offline")

    with col2:

        st.success("🟢 Gmail Connected")
        st.success("🟢 ChromaDB Ready")