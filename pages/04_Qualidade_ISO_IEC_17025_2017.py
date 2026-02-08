import streamlit as st

st.set_page_config(
    page_title="Qualidade ISO IEC 17025:2017",
    page_icon="✅",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        4️⃣ Qualidade ISO IEC17025:2017
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Consolidação dos requisitos essenciais de qualidade e integridade técnica no laboratório,
        garantindo rastreabilidade, registros completos e robustez na emissão de relatórios.
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
    card("🎚️ Nível de dificuldade", "Fácil")

with c3:
    card("🎓 Modalidade", "Treinamento interno +<br>prática operacional")

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
- Competência e autorização  
- Rastreabilidade metrológica  
- Avaliação de métodos  
- Registros técnicos completos  
- Revisão de relatórios  
- Controle de não conformidade  
- Imparcialidade e confidencialidade  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")
    st.markdown(
        """
- Cursos internos do LABELO (Qualidade)  
- Participação em Auditorias Internas  
- Execução das atividades do laboratório (aplicação prática contínua)  
        """
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Avaliação teórica  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "Módulo voltado à consolidação dos requisitos de qualidade aplicados no dia a dia do laboratório, "
        "com ênfase na geração de evidências auditáveis, rastreabilidade e padronização dos registros técnicos."
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
