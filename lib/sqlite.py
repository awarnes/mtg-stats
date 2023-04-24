import os
import sqlite3
import streamlit as st
from pathlib import Path

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class AllPrintings():
    def __init__(self):
        self.connection = sqlite3.connect(
            os.path.join(
                Path(__file__).parent,
                'db/AllPrintings.sqlite'
            ))

        self.connection.row_factory = dict_factory

    @st.cache_data
    def query(_self):
        with _self.connection:
            result = _self.connection.execute("SELECT * FROM cards WHERE subtypes = 'Angel'")
            return result.fetchall()

    def select_cards_where(self, filter_columns, column: str, value: str):
        with self.connection as conn:
            res = conn.execute("SELECT :filter_columns FROM cards WHERE :column = :value", {'filter_columns': filter_columns, 'column': column, 'value': value})
            return res.fetchall()

