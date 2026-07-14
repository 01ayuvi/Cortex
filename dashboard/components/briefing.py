import streamlit as st


def render_briefing(tasks):

    st.subheader("📋 Today's Briefing")

    if tasks:

        for task in tasks:

            task_name = task["task"]
            priority = task["priority"]

            if priority == "HIGH":

                st.success(
                    f"🔥 {task_name}"
                )

            elif priority == "MEDIUM":

                st.info(
                    f"📌 {task_name}"
                )

            else:

                st.warning(
                    f"📄 {task_name}"
                )

    else:

        st.info(
            "No tasks available."
        )

    st.divider()