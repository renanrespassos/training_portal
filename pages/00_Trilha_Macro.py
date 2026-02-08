import streamlit as st

st.set_page_config(page_title="Trilha Macro", page_icon="🧭", layout="wide")

# ======================
# Header
# ======================
st.markdown(
    """
    <div style="padding: 14px 18px; border-radius: 14px; border: 1px solid rgba(49,51,63,0.2);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.1;">🧭 Trilha de Capacitação</div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Visão Macro — clique em cada módulo para abrir o detalhamento (conteúdo, cursos, tempo e avaliação).
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ======================
# Cards (clicáveis)
# ======================
sequence = [
    ("1️⃣", "Fundamentos de Metrologia em Radio Frequência", "Base de medição em RF: espectro, boas práticas e setup de analisador.", "pages/01_Fundamentos_RF.py"),
    ("2️⃣", "Tecnologias de Comunicação Sem Fio", "Visão aplicada de 2G/3G/4G, Wi-Fi, BT, LoRa, ZigBee e spread spectrum.", "pages/02_Tecnologias_Wireless.py"),
    ("3️⃣", "Configuração de Amostras", "PuTTY/TeraTerm, logs, comandos e preparação de DUT (incl. ESP32).", "pages/03_Configuracao_Amostras.py"),
    ("4️⃣", "Qualidade ISO IEC 17025:2017", "Evidências, rastreabilidade e revisão de relatórios alinhado à 17025.", "pages/04_Qualidade_17025.py"),
    ("5️⃣", "Regulatório Anatel", "Atos aplicáveis e mapeamento requisito → evidência → conclusão.", "pages/05_Regulatorio_Anatel.py"),
    ("6️⃣", "Ensaios em Estações Terminais de Acesso (ETA)", "Execução prática de ensaios (ex.: CMW500/MT8821) e relatórios.", "pages/06_Ensaios_ETA.py"),
    ("7️⃣", "IPv6 & Redes", "IPv6 Ready, RFC 8200 e topologias de teste com evidências.", "pages/07_IPv6_e_Redes.py"),
    ("8️⃣", "Soft Skills", "Liderança, gestão de projetos, IE, comunicação e inglês.", "pages/08_Soft_Skills.py"),
]

# Layout em 2 colunas
left, right = st.columns(2, gap="large")

def render_card(col, emoji, title, subtitle, page_path):
    with col:
        with st.container(border=True):
            st.markdown(f"### {emoji} {title}")
            st.caption(subtitle)
            c1, c2 = st.columns([1, 1])
            with c1:
                if st.button("Abrir módulo", use_container_width=True, key=f"open_{title}"):
                    st.switch_page(page_path)
            with c2:
                st.button("Ver detalhes", use_container_width=True, disabled=True, key=f"details_{title}")

# Render cards alternando colunas
for i, (emoji, title, subtitle, page_path) in enumerate(sequence):
    render_card(left if i % 2 == 0 else right, emoji, title, subtitle, page_path)

st.write("")
st.info("💡 Dica: os módulos abrem como subpáginas no menu lateral. Esta tela é a visão executiva (macro).")

