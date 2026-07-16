import streamlit as st
from services.api import complete_task


def render_task_cards(tasks):

    st.subheader("📌 Tasks")

    if not tasks:
        st.info("No tasks available.")
        return

    for task in tasks:

        priority = task["priority"]
        status = task.get("status", "PENDING")

        if priority == "HIGH":
            badge = "🔥 HIGH"
        elif priority == "MEDIUM":
            badge = "📌 MEDIUM"
        else:
            badge = "📄 LOW"

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"### {task['task']}")
                st.caption(badge)

                if task.get("category"):
                    st.write(f"**Category:** {task['category']}")

                if task.get("deadline"):
                    st.write(f"📅 {task['deadline']}")

            with col2:

                if status == "COMPLETED":
                    st.success("Done")
                else:
                    if st.button(
                        "Complete",
                        key=f"card_{task['id']}"
                    ):
                        complete_task(task["id"])
                        st.rerun()