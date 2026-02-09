import streamlit as st

st.set_page_config(
    page_title="Regulatório Anatel",
    page_icon="📜",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        5️⃣ Regulatório Anatel
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Interpretação prática de requisitos regulatórios aplicáveis a produtos de telecomunicações,
        com foco em mapeamento de evidências e consistência técnica na homologação.
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
    card("⏱️ Tempo de desenvolvimento", "6 meses")

with c2:
    card("🎚️ Nível de dificuldade", "Médio")

with c3:
    card("🎓 Modalidade", "Leitura orientada +<br>estudo de casos")

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
- Ato 14448  
- Ato 3151  
- Ato 237  
- Ato 7971  
- Interpretação normativa  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown(
        """
- Leitura orientada dos Atos normativos (Ato 14448, 3151, 237, 7971)  
- Interpretação prática de requisitos aplicáveis a produtos de telecomunicações  
- Estudo de casos reais de certificação e homologação  
        """
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Mapear requisito x evidência  
- Interpretar requisitos sozinho  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "Não foram identificados cursos específicos voltados para este item. O desenvolvimento do conhecimento ocorre "
        "principalmente por leitura direta dos Atos normativos e pela interpretação prática dos requisitos regulatórios aplicáveis."
    )
    st.write(
        "A consolidação do aprendizado dá-se na aplicação cotidiana das normas, durante a análise de produtos, elaboração de relatórios "
        "e enquadramento técnico frente às exigências da regulamentação vigente."
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
