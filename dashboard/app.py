import streamlit as st
import pandas as pd
import sys
import os
import requests

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

# ====================================
# LOAD TASKS
# ====================================

try:

    response = requests.get(
        "http://127.0.0.1:8000/tasks"
    )

    tasks = response.json()

except Exception as e:

    st.error(
        f"API Error: {e}"
    )

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
        with st.spinner("Running Cortex..."):
            try:
                response = requests.post(
                "http://127.0.0.1:8000/run-cortex"
                )

                result = response.json()
                st.success(
                    f"Processed {result['emails_processed']} emails | Added {result['new_tasks']} tasks"
                )

                st.info(
                    "Refresh the dashboard to see updated results."
                )

            except Exception as e:

                st.error(
                    f"Pipeline Error: {e}"
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

st.subheader("✅ Task Actions")

for task in tasks:

    col1, col2 = st.columns([4, 1])

    with col1:

        status = task.get(
            "status",
            "PENDING"
        )

        if status == "COMPLETED":

            st.success(
                f"✅ {task['task']}"
            )

        else:

            st.write(
                f"🔲 {task['task']}"
            )

    with col2:

        if status != "COMPLETED":

            if st.button(
                "Complete",
                key=f"complete_{task['id']}"
            ):

                requests.put(
                    f"http://127.0.0.1:8000/tasks/{task['id']}",
                    params={
                        "status": "COMPLETED"
                    }
                )

                st.rerun()

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

st.subheader("✅ Task Actions")

for task in tasks:

    col1, col2 = st.columns([4, 1])

    with col1:

        st.write(
            f"{task['task']} "
            f"({task.get('status', 'PENDING')})"
        )

    with col2:

        if task.get("status") != "COMPLETED":

            if st.button(
                "Complete",
                key=f"task_{task['id']}"
            ):

                requests.put(
                    f"http://127.0.0.1:8000/tasks/{task['id']}",
                    params={
                        "status": "COMPLETED"
                    }
                )

                st.rerun()

# ====================================
# FOOTER
# ====================================

st.caption(
    "Cortex AI Assistant • Gmail + Llama 3 + SQLite + Streamlit"
)