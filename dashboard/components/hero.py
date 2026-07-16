import streamlit as st


def render_hero(total_tasks, high_priority):

    st.markdown(
        f"""
        ## 👋 Welcome Back!

        Cortex analyzed your inbox and found **{total_tasks} actionable tasks**.

        🔥 **{high_priority} High Priority**

        ---
        """
    )