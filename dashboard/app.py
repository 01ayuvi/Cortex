import streamlit as st
import pandas as pd
import sys
import os

from styles.theme import apply_theme
from components.sidebar import render_sidebar
from components.metric_cards import render_metric_cards
from components.controls import render_controls
from components.task_actions import render_task_actions

from services.api import (
    get_tasks,
    run_cortex,
    complete_task
)

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Cortex Dashboard",
    page_icon="🧠",
    layout="wide"
)
apply_theme()
# ====================================
# CUSTOM STYLING
# ====================================


# ====================================
# LOAD TASKS
# ====================================

try:
    tasks = get_tasks()

except Exception as e:
    st.error(f"API Error: {e}")
    tasks = []

# ====================================
# METRICS
# ====================================

total_tasks = len(tasks)

high_priority = sum(
    1 for task in tasks
    if task["priority"] == "HIGH"
)
deadlines = sum(
    1 for task in tasks
    if task["deadline"]
)

# ====================================
# SIDEBAR
# ====================================

render_sidebar(
    total_tasks,
    high_priority,
    deadlines
)

# ====================================
# HEADER
# ====================================

st.title("🧠 Cortex AI Assistant")
st.caption(
    "AI-Powered Email Intelligence Dashboard"
)

# ====================================
# CONTROL PANEL
# ====================================

render_controls()


# ====================================
# DAILY BRIEFING
# ====================================

st.subheader("📋 Today's Briefing")

if tasks:

    for task in tasks:

        task_name = task["task"]
        priority = task["priority"]

        if priority == "HIGH":
            st.success(f"🔥 {task_name}")

        elif priority == "MEDIUM":
            st.info(f"📌 {task_name}")

        else:
            st.warning(f"📄 {task_name}")

else:

    st.info(
        "No tasks available."
    )

st.divider()

# ====================================
# TASK ACTIONS
# ====================================

render_task_actions(tasks)

st.divider()

# ====================================
# TASK DATAFRAME
# ====================================

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

    # -------------------------
    # SEARCH
    # -------------------------

    search_term = st.text_input(
        "🔍 Search Tasks"
    )

    if search_term:

        df = df[
            df["Task"]
            .str.contains(
                search_term,
                case=False,
                na=False
            )
        ]

    # -------------------------
    # FILTER
    # -------------------------

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
        width="stretch",
        hide_index=True
    )

else:

    st.warning(
        "No tasks found."
    )

# ====================================
# PRIORITY ANALYTICS
# ====================================

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


# ====================================
# FOOTER
# ====================================

st.caption(
    "Cortex AI Assistant • Gmail + Llama 3 + SQLite + Streamlit"
)