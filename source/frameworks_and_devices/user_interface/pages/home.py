import streamlit as st


def display():
    st.data_editor(
        data=[{"dmeo": 1}, {"dmeo": 1}, {"dmeo": 1}],
        use_container_width=True,
    )
