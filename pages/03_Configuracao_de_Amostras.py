import streamlit as st

st.set_page_config(
    page_title="Configuração de Amostras",
    page_icon="🧰",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        3️⃣ Configuração de Amostras
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Competências práticas para preparar, configurar e diagnosticar amostras (DUT) em bancada,
        garantindo estabilidade de firmware, comunicação, logs e evidências consistentes para ensaio.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ======================
# KPIs (cards iguais)
# ======================
c1, c2, c3 = st.columns(3)

def card(title, value):
    st.markdown(
        f"""
        <div style="
            padding:18px;
            border-radius:14px;
            border:1px solid rgba(49,51,63,0.2);
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:14px; opacity:0.75;">{title}</div>
            <div style="
                font-size:22px;
                font-weight:700;
                margin-top:6px;
                line-height:1.2;
            ">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c1:
    card("⏱️ Tempo de desenvolvimento", "1 ano")

with c2:
    card("🎚️ Nível de dificuldade", "Difícil")

with c3:
    card("🎓 Modalidade", "E-learning +<br>prática supervisionada")

st.write("")

# ======================
# Conteúdo em abas
# ======================
tab1, tab2, tab3, tab4 = st.tabs(
    ["📖 Conteúdo", "🎓 Formas de Aprendizado", "✅ Avaliação", "📝 Observações"]
)

with tab1:
    st.subheader("📖 Conteúdo")
    st.markdown(
        """
- Preparação de amostras para ensaio  
- Configuração e instalação de firmwares  
- Logs, comandos AT e ADB  
- Configuração via PuTTY e TeraTerm  
- Comunicação serial (UART, SPI e outros padrões)  
- ESP32, ARM e outros microcontroladores  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Guias / Cursos (online):**")
    st.markdown(
        """
- 📘 [Android Debug Bridge (ADB) – Documentação oficial](https://developer.android.com/tools/adb?hl=pt-br)  
- 🎓 [Embedded Systems – edX (catálogo de cursos)](https://www.edx.org/learn/embedded-systems)  
        """
    )

    st.markdown("**Prática aplicada (LABELO):**")
    st.markdown(
        """
- Execução supervisionada na prática (bancada / rotina real)  
- Aprendizado baseado em problemas e soluções (troubleshooting guiado)  
        """
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Configurar amostra sozinho  
- Coletar logs válidos  
- Enviar comandos através de diferentes plataformas  
- Documentar evidências  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "O desenvolvimento das competências requer conhecimento prático aplicado, especialmente na identificação e resolução "
        "de problemas específicos de cada arquitetura de hardware e das particularidades de implementação de cada cliente ou projeto."
    )
    st.write(
        "Embora cursos e treinamentos forneçam embasamento teórico relevante — como fundamentos de firmware, protocolos de comunicação, "
        "logs e ferramentas de debug —, a consolidação do aprendizado ocorre de forma mais efetiva por meio da prática contínua em bancada "
        "e da vivência em situações reais."
    )

st.write("")
st.divider()

# ======================
# Rodapé + botão retorno
# ======================
col1, col2 = st.columns([6, 1])

with col1:
    st.caption("Versão do módulo: v1 • Atualizado conforme trilha interna • LABELO")

with col2:
    if st.button("⬅️ Voltar"):
        st.switch_page("pages/00_Trilha_Macro.py")
