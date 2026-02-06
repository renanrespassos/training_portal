import streamlit as st
from pathlib import Path

st.title("⚙️ Admin")

p = Path("catalog.yml")

if p.exists():
    st.code(p.read_text(), language="yaml")
else:
    st.error("catalog.yml não encontrado.")
