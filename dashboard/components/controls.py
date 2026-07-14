import streamlit as st

from services.api import run_cortex


def render_controls():

    st.subheader("⚡ Cortex Controls")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🚀 Run Cortex Pipeline"):

            with st.spinner("Running Cortex..."):

                try:

                    result = run_cortex()

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

        if st.button("🔄 Refresh Dashboard"):

            st.rerun()

    st.divider()