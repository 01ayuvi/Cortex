import streamlit as st
import pandas as pd


def render_task_table(tasks):

    st.subheader("📌 Task Dashboard")

    if tasks:

        df = pd.DataFrame(tasks)

        df = df.rename(
            columns={
                "task": "Task",
                "deadline": "Deadline",
                "priority": "Priority",
                "category": "Category",
                "status": "Status"
            }
        )

        if "id" in df.columns:
            df = df.drop(columns=["id"])

        search_term = st.text_input(
            "🔍 Search Tasks"
        )

        if search_term:

            df = df[
                df["Task"].str.contains(
                    search_term,
                    case=False,
                    na=False
                )
            ]

        priority_filter = st.selectbox(
            "Filter Priority",
            [
                "ALL",
                "HIGH",
                "MEDIUM",
                "LOW"
            ]
        )

        if priority_filter != "ALL":

            df = df[
                df["Priority"]
                == priority_filter
            ]

        st.dataframe(
            df,
            hide_index=True,
            width="stretch"
        )

    else:

        st.warning(
            "No tasks found."
        )