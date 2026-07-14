import streamlit as st


def render_metric_cards(total_tasks, high_priority, deadlines):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📋 Total Tasks",
            total_tasks
        )

    with col2:
        st.metric(
            "🔥 High Priority",
            high_priority
        )

    with col3:
        st.metric(
            "📅 Deadlines",
            deadlines
        )

    st.divider()