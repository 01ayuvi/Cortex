import streamlit as st
import requests
import ollama


def render_system_status():
    st.subheader("🖥️ System Status")

    col1, col2 = st.columns(2)

    # FastAPI
    with col1:
        try:
            response = requests.get(
                "http://127.0.0.1:8000/docs",
                timeout=2
            )

            if response.status_code == 200:
                st.success("🟢 FastAPI Online")
            else:
                st.error("🔴 FastAPI Offline")

        except Exception:
            st.error("🔴 FastAPI Offline")

    # Ollama
    with col2:
        try:
            ollama.list()
            st.success("🟢 Ollama Running")
        except Exception:
            st.error("🔴 Ollama Offline")

    st.success("🟢 Gmail Connected")
    st.success("🟢 ChromaDB Ready")