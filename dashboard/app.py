import streamlit as st
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from database.db import get_tasks

st.set_page_config(
    page_title="Cortex Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Cortex AI Assistant")

st.subheader("Stored Tasks")

tasks = get_tasks()

if not tasks:
    st.info("No tasks found.")
else:

    for task in tasks:

        task_id = task[0]
        task_name = task[1]
        deadline = task[2]
        priority = task[3]

        st.write(f"### [{priority}] {task_name}")

        if deadline:
            st.write(f"Deadline: {deadline}")

        st.divider()