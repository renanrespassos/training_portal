import streamlit as st

st.set_page_config(
    page_title="Fundamentos de Metrologia em RF",
    page_icon="📡",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        1️⃣ Fundamentos de Metrologia em Radio Frequência
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Base teórica e prática para medições em RF: instrumentação, parâmetros de medição e boas práticas laboratoriais.
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
    card("⏱️ Tempo de desenvolvimento", "3 meses")

with c2:
    card("🎚️ Nível de dificuldade", "Médio")

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
- Conceitos básicos de física e elétrica  
- Conceitos de rádio frequência e espectro  
- Boas práticas de medição  
- Configuração de analisador de espectro  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Cursos (online):**")

    st.markdown(
        """
- ✅ **Grátis** — [Fundamentos de RF (Anritsu)](https://www.anritsu.com/en-us/test-measurement/support/training-and-education/elearning/rf-fundamentals)  
- ✅ **Grátis** — [Introdução ao Analisador de Espectro (Anritsu)](https://www.anritsu.com/en-us/test-measurement/support/training-and-education/elearning/spectrum-analysis/introduction-to-spectrum-analysis)  
        """
    )

    st.markdown("**Prática supervisionada (LABELO):**")
    st.markdown(
        "- Execução supervisionada na prática (bancada / rotina real de medição)"
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Configurar medição sozinho  
- Repetibilidade de medição  
- Análise de problemas comuns  
- Avaliação teórica  
        """
    )

with tab4:
    st.subheader("📝 Observações")

    st.write(
        "Conhecimento teórico e prático dos fundamentos de medição em radiofrequência, "
        "abrangendo conceitos básicos de instrumentação, parâmetros de medição e boas práticas laboratoriais."
    )

    st.write(
        "Esse conhecimento encontra-se amplamente consolidado no LABELO, especialmente entre profissionais "
        "com experiência nas atividades de calibração em radiofrequência."
    )

st.write("")
st.divider()

# ======================
# Rodapé + botão retorno
# ======================
col1, col2 = st.columns([6,1])

with col1:
    st.caption(
        "Versão do módulo: v1 • Atualizado conforme trilha interna • LABELO"
    )

with col2:
    if st.button("⬅️ Voltar"):
        st.switch_page("pages/00_Trilha_Macro.py")
