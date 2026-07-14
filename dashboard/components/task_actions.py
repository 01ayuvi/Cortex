import streamlit as st

from services.api import complete_task


def render_task_actions(tasks):

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

                    complete_task(task["id"])

                    st.rerun()

    st.divider()