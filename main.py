import streamlit as st

from lib.sqlite import AllPrintings
from lib.constants import (
    COLUMNS,
    OPERATIONS
)

PRODUCTION = False

sq = AllPrintings()

try:
    with st.spinner():
        data = sq.query()

    with st.sidebar:
        st.header('Filters')
        column_selections = st.multiselect("Columns", COLUMNS)

    apple = st.dataframe(data)
    print(apple)
    st.divider()


    st.radio('Operation', OPERATIONS, horizontal=True)

    st.bar_chart(data, y='colors')

except Exception as error:
    if PRODUCTION:
        st.error(f'We encountered an error...\nPlease reload the page and try again.')
    else:
        st.exception(error)