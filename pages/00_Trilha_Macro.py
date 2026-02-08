import streamlit as st

st.set_page_config(page_title="Trilha Macro", page_icon="🧭", layout="wide")

st.markdown(
    """
    <div style="padding: 14px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.1;">🧭 Trilha de Capacitação – Visão Macro</div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Clique em cada módulo para abrir o detalhamento (Conteúdo, Cursos, Tempo e Avaliação).
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

sequence = [
    ("1️⃣", "Fundamentos de Metrologia em Radio Frequência", "pages/01_Fundamentos_Metrologia_RF.py"),
    ("2️⃣", "Tecnologias de Comunicação Sem Fio", "pages/02_Tecnologias_Comunicacao_Sem_Fio.py"),
    ("3️⃣", "Configuração de Amostras", "pages/03_Configuracao_de_Amostras.py"),
    ("4️⃣", "Qualidade ISO IEC17025:2017", "pages/04_Qualidade_ISO_IEC_17025_2017.py"),
    ("5️⃣", "Regulatório Anatel", "pages/05_Regulatorio_Anatel.py"),
    ("6️⃣", "Ensaios em Estações Terminais de Acesso (ETA)", "pages/06_Ensaios_ETA.py"),
    ("7️⃣", "IPv6 & Redes", "pages/07_IPv6_e_Redes.py"),
    ("8️⃣", "Soft Skills", "pages/08_Soft_Skills.py"),
]

left, right = st.columns(2, gap="large")

def card(col, num, title, page_path):
    with col:
        with st.container(border=True):
            st.markdown(f"### {num} {title}")
            st.caption("Abrir detalhamento do módulo (Conteúdo • Cursos • Tempo • Avaliação).")
            if st.button("Abrir módulo", use_container_width=True, key=f"btn_{num}"):
                st.switch_page(page_path)

for i, (num, title, page_path) in enumerate(sequence):
    card(left if i % 2 == 0 else right, num, title, page_path)

st.write("")
st.info("✅ Dica: após renomear os arquivos, se algum botão não abrir, é só revisar o caminho `pages/...` acima.")
