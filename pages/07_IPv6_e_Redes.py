import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Qualidade 17025", page_icon="📦", layout="wide")

catalog = yaml.safe_load(Path("catalog.yml").read_text(encoding="utf-8"))
modules = catalog.get("modules", [])

MODULE_NAME = "Qualidade 17025"
mod = next((m for m in modules if m.get("name") == MODULE_NAME), None)

st.title(f"📦 {MODULE_NAME}")

if not mod:
    st.error(f"Módulo '{MODULE_NAME}' não encontrado no catalog.yml.")
    st.stop()

st.subheader("📖 Conteúdo")
for item in mod.get("content", []):
    st.markdown(f"- {item}")

st.subheader("🎓 Cursos")
for c in mod.get("courses", []):
    st.markdown(f"- [{c.get('name','Curso')}]({c.get('url','#')})")

st.subheader("⏱️ Tempo")
st.info(mod.get("time", "Não informado"))

st.subheader("✅ Avaliação")
for item in mod.get("evaluation", []):
    st.markdown(f"- {item}")
