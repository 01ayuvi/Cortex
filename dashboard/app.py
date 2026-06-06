import streamlit as st
import pandas as pd
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

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Cortex Dashboard",
    page_icon="🧠",
    layout="wide"
)

# ====================================
# LOAD TASKS
# ====================================

tasks = get_tasks()

# ====================================
# METRICS
# ====================================

total_tasks = len(tasks)

high_priority = sum(
    1 for task in tasks
    if task[3] == "HIGH"
)

deadlines = sum(
    1 for task in tasks
    if task[2]
)

# ====================================
# SIDEBAR
# ====================================

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
        "Phase 7 Dashboard"
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

st.subheader("⚡ Cortex Controls")

col1, col2 = st.columns(2)

with col1:
    if st.button("Run Cortex Pipeline"):
        st.success(
            "Pipeline integration coming soon."
        )

with col2:
    if st.button("Refresh Dashboard"):
        st.rerun()

st.divider()

# ====================================
# KPI CARDS
# ====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Tasks",
        total_tasks
    )

with col2:
    st.metric(
        "High Priority",
        high_priority
    )

with col3:
    st.metric(
        "Deadlines",
        deadlines
    )

st.divider()

# ====================================
# DAILY BRIEFING
# ====================================

st.subheader("📋 Today's Briefing")

if tasks:

    for task in tasks:

        task_name = task[1]
        priority = task[3]

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
# TASK DATAFRAME
# ====================================

st.subheader("📌 Task Dashboard")

if tasks:

    df = pd.DataFrame(
        tasks,
        columns=[
            "ID",
            "Task",
            "Deadline",
            "Priority"
        ]
    )

    df = df.drop(
        columns=["ID"]
    )

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
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No tasks found."
    )

st.divider()

# ====================================
# PRIORITY ANALYTICS
# ====================================

st.subheader("📊 Priority Analytics")

if tasks:

    analytics_df = pd.DataFrame(
        tasks,
        columns=[
            "ID",
            "Task",
            "Deadline",
            "Priority"
        ]
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
        use_container_width=True
    )

else:

    st.info(
        "No analytics available."
    )

st.divider()

# ====================================
# FOOTER
# ====================================

st.caption(
    "Cortex AI Assistant • Gmail + Llama 3 + SQLite + Streamlit"
)