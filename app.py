import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(
    page_title="Portal de Treinamento – Telecom",
    page_icon="🧭",
    layout="wide"
)

@st.cache_data
def load_catalog():
    path = Path("catalog.yml")
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8"))

catalog = load_catalog()

st.title("🧭 Portal da Trilha de Capacitação")
st.write(
    "Bem-vindo ao portal de desenvolvimento técnico.\n\n"
    "Use o menu lateral para navegar entre a visão macro e os detalhes (micro)."
)

if catalog:
    prog = catalog.get("program", {})
    st.info(
        f"📚 {prog.get('title','')}  \n"
        f"⏱️ Duração: {prog.get('duration_weeks','?')} semanas  \n"
        f"📅 Última atualização: {prog.get('last_update','')}"
    )
else:
    st.warning("Arquivo catalog.yml não encontrado.")

