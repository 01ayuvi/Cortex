import streamlit as st
import pandas as pd
import sys
import os

from styles.theme import apply_theme
from components.sidebar import render_sidebar
from components.metric_cards import render_metric_cards
from components.controls import render_controls
from components.task_actions import render_task_actions
from components.briefing import render_briefing
from components.task_table import render_task_table
from components.analytics import render_analytics
from components.hero import render_hero
from components.system_status import render_system_status
from components.system_status import render_system_status


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

render_hero()

# ====================================
# CONTROL PANEL
# ====================================

render_controls()

render_system_status()


# ====================================
# DAILY BRIEFING
# ====================================

render_briefing(tasks)

# ====================================
# TASK ACTIONS
# ====================================

render_task_actions(tasks)

st.divider()

# ====================================
# TASK DATAFRAME
# ====================================

render_task_table(tasks)

# ====================================
# PRIORITY ANALYTICS
# ====================================

render_analytics(tasks)

# ====================================
# FOOTER
# ====================================

st.caption(
    "Cortex AI Assistant • Gmail + Llama 3 + SQLite + Streamlit"
)