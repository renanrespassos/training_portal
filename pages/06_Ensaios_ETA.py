import streamlit as st

st.set_page_config(
    page_title="Ensaios em ETA",
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
        6️⃣ Ensaios em Estações Terminais de Acesso (ETA)
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Competências para execução completa de ensaios em tecnologias celulares (2G/3G/4G),
        incluindo configuração de rádios bases, definição de cenários e análise crítica dos resultados.
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
    card("🎓 Modalidade", "Fabricante + prática<br>supervisionada")

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
- ETSI 151 – 2G  
- ETSI 134 – 3G  
- ETSI 136 – 4G  
- Configuração CMW500  
- Configuração MT8821  
- Execução de ensaios OTA e conduzidos  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Materiais e apoio do fabricante:**")
    st.markdown(
        """
- 📘 [MT8821C – Página do produto / referências (Anritsu)](https://www.anritsu.com/en-us/test-measurement/products/mt8821c)  
- Aprendizado direto com o fabricante (documentações, guias, notas técnicas e suporte)  
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
- Executar ensaio completo  
- Operação das rádios bases  
- Análise dos resultados gerados pelos padrões  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "Conteúdo extremamente denso e específico, uma vez que as normas aplicáveis a cada tecnologia contemplam grande volume "
        "de requisitos técnicos, cenários de ensaio e variações operacionais (por exemplo, a tecnologia 4G possui especificações "
        "muito extensas)."
    )
    st.write(
        "As especificações são extensas por tratarem múltiplos casos de uso, combinações de bandas, modos de operação e condições de teste."
    )
    st.write(
        "Não foram identificados cursos específicos dedicados exclusivamente ao estudo aprofundado dessas normas. Dessa forma, o conhecimento "
        "é adquirido principalmente por meio de leitura dirigida das especificações, interpretação técnica dos requisitos e aplicação prática "
        "durante a execução dos ensaios laboratoriais."
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
