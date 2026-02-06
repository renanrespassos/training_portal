import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Trilha Macro", layout="wide")

catalog = yaml.safe_load(Path("catalog.yml").read_text(encoding="utf-8"))
modules = catalog["modules"]

st.title("🧭 Trilha de Capacitação – Visão Macro")

cols = st.columns(2)

for i, m in enumerate(modules):
    with cols[i % 2]:
        st.markdown(f"### 📦 {m['name']}")
        st.write("Clique no menu lateral para ver detalhes.")
