import streamlit as st
from frameworks_and_devices.user_interface.organisms import (
    add_entry_dialog,
    entries_data_editor,
)


def display():
    st.title(
        body="Entries",
    )

    if st.button(
        label="Add entry",
        use_container_width=True,
    ):
        add_entry_dialog.display()

    entries_data_editor.display()
