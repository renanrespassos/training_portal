import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="IPv6 Ready", layout="wide")

catalog = yaml.safe_load(Path("catalog.yml").read_text(encoding="utf-8"))
modules = catalog.get("modules", [])

st.title("🌐 IPv6 Ready / Redes")

net = [m for m in modules if m["area"] == "Redes"]

for m in net:
    with st.expander(f"Semana {m['week']} • {m['title']}"):
        st.write(m["objective"])
