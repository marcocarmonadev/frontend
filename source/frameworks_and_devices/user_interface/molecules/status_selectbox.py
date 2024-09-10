import streamlit as st
from frameworks_and_devices.external_interfaces.backend import models


def display():
    st.selectbox(
        label="Status",
        options=[status for status in models.Status],
        index=0,
        key="status",
    )
