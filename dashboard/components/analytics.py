import streamlit as st
import pandas as pd


def render_analytics(tasks):

    st.subheader("📊 Priority Analytics")

    if tasks:

        analytics_df = pd.DataFrame(tasks)

        analytics_df = analytics_df.rename(
            columns={
                "priority": "Priority"
            }
        )

        priority_counts = (
            analytics_df["Priority"]
            .value_counts()
            .rename_axis("Priority")
            .reset_index(name="Count")
        )

        st.dataframe(
            priority_counts,
            hide_index=True,
            width="stretch"
        )

    else:

        st.info(
            "No analytics available."
        )