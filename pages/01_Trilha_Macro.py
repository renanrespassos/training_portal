import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Trilha Macro", layout="wide")

@st.cache_data
def load_catalog():
    return yaml.safe_load(Path("catalog.yml").read_text(encoding="utf-8"))

catalog = load_catalog()
modules = catalog.get("modules", [])

st.title("📍 Visão Macro da Trilha")

for m in modules:
    with st.expander(f"Semana {m['week']} • {m['title']}"):
        st.write(f"**Objetivo:** {m['objective']}")

        st.write("**Aprendizado:**")
        for i in m["what_you_learn"]:
            st.write(f"- {i}")

        st.write(f"⏱️ Tempo: {m['estimated_time_hours']}h")
