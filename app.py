import streamlit as st
import pyperclip
import hson
from styles import CUSTOM_CSS


def jsonify():
    json_value = hson.jsonify(headers)
    st.session_state["json_value"] = json_value


def copy():
    pyperclip.copy(st.session_state["json_value"])

st.set_page_config(page_title="HSON",
                   page_icon=":performing_arts:",
                   layout="wide")

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title(":performing_arts: HTTPS headers to JSON")

headers_col, json_col = st.columns(2)

with headers_col:
    headers = st.text_area("Headers",
                           height=400)
    st.button("Jsonify",
              on_click=jsonify)

if "json_value" not in st.session_state:
    st.session_state["json_value"] = " "

with json_col:
    st.text_area("JSON",
                 height=400,
                 value=st.session_state["json_value"])

    st.button("Copy",
              on_click=copy)