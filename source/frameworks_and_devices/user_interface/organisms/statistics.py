import streamlit as st
from frameworks_and_devices.external_interfaces import get_backend_client


def display():
    backend_client = get_backend_client()
    entries_statistics = backend_client.get_entries_statistics()
    column1, column2, column3 = st.columns(3)

    column1.metric(
        label="Income amount",
        value=f'${entries_statistics["income_amount"]}',
    )

    column2.metric(
        label="Expense amount",
        value=f'${entries_statistics["expense_amount"]}',
    )

    column3.metric(
        label="Total amount",
        value=f'${entries_statistics["total_amount"]}',
    )
