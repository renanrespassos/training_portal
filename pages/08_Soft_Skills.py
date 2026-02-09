import streamlit as st

st.set_page_config(
    page_title="Soft Skills",
    page_icon="🧠",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        8️⃣ Soft Skills
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Desenvolvimento de competências comportamentais para fortalecer liderança, gestão, comunicação e influência,
        com aplicação direta na rotina de projetos, reuniões técnicas e relacionamento com stakeholders.
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
    card("🎓 Modalidade", "Cursos + prática<br>contínua")

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
- Liderança  
- Gestão de projetos  
- Inteligência emocional  
- Comunicação técnica  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Cursos (fornecedor PUCRS – opções consideradas):**")
    st.markdown(
        """
- 💳 **R$ 468** — [Liderança: como inspirar e influenciar positivamente (PUCRS)](https://online.pucrs.br/certificacao-profissional/lideranca-como-inspirar-e-influenciar-positivamente-1?utm_variant_id=24&utm_variant=checkoutCD)  
- 💳 **R$ 720** — [Gestão de Conflitos, Gestão de Crise e Tomada de Decisão (PUCRS)](https://online.pucrs.br/certificacao-profissional/gestao-de-conflitos-gestao-de-crise-e-tomada-de-decisao?utm_variant_id=24&utm_variant=checkoutCD)  
- 💳 **R$ 1308** — [Gestão Lean para Melhoria Contínua (PUCRS)](https://online.pucrs.br/certificacao-profissional/gestao-lean-para-melhoria-continua?utm_variant_id=24&utm_variant=checkoutCD)  
        """
    )

    st.markdown("**Aplicação prática sugerida (interno):**")
    st.markdown(
        """
- Condução de reuniões técnicas (pauta, tempo, decisões e follow-up)  
- Gestão de cronogramas e alinhamento de prioridades com stakeholders  
- Rotina de feedback (1:1) e desenvolvimento de time  
- Suporte à equipe comercial com postura de facilitação e clareza técnica  
        """
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Conduzir reunião técnica  
- Apresentar resultados  
- Gerenciar cronograma e a equipe  
- Ser um facilitador para equipe comercial  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "Os cursos voltados ao desenvolvimento de soft skills e liderança apresentam ferramentas, metodologias e linhas de raciocínio "
        "aplicáveis ao cotidiano profissional, contribuindo para a estruturação de práticas de gestão e relacionamento interpessoal."
    )
    st.write(
        "Entretanto, a consolidação da expertise nessas competências ocorre predominantemente por meio da vivência prática e da experiência "
        "acumulada ao longo do tempo, uma vez que envolvem interação direta com pessoas, contextos variáveis e situações cuja previsibilidade "
        "não é exata."
    )
    st.write(
        "Foram consideradas opções de capacitação da PUCRS; porém, existem alternativas com outros fornecedores que oferecem plataformas com "
        "diversas soft skills por valores menores."
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
