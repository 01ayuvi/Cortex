import streamlit as st


def render_sidebar(total_tasks, high_priority, deadlines):
    with st.sidebar:

        st.title("🧠 Cortex")

        st.markdown(
            "AI-Powered Email Intelligence Assistant"
        )

        st.divider()

        st.metric(
            "Total Tasks",
            total_tasks
        )

        st.metric(
            "High Priority",
            high_priority
        )

        st.metric(
            "Deadlines",
            deadlines
        )

        st.divider()

        st.caption(
            "Phase 14 Dashboard"
        )