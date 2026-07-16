import streamlit as st
import pandas as pd


def render_analytics(tasks):

    st.subheader("📊 Analytics")

    if not tasks:
        st.info("No analytics available.")
        return

    df = pd.DataFrame(tasks)

    # Priority Distribution
    st.markdown("### Priority Distribution")

    priority_counts = (
        df["priority"]
        .value_counts()
    )

    st.bar_chart(priority_counts)

    # Status Distribution
    if "status" in df.columns:

        st.markdown("### Task Status")

        status_counts = (
            df["status"]
            .value_counts()
        )

        st.bar_chart(status_counts)