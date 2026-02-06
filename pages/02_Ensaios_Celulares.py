import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Ensaios Celulares", layout="wide")

catalog = yaml.safe_load(Path("catalog.yml").read_text(encoding="utf-8"))
modules = catalog.get("modules", [])

st.title("📡 Ensaios Celulares")

cell = [m for m in modules if m["area"] == "Celular"]

for m in cell:
    with st.expander(f"Semana {m['week']} • {m['title']}"):
        st.write(m["objective"])

        st.write("**Cursos externos:**")
        for c in m["external_courses"]:
            st.markdown(f"[{c['name']}]({c['url']})")
