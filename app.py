import streamlit as st

st.set_page_config(
    page_title="Portal de Capacitação – Telecom",
    page_icon="📘",
    layout="wide"
)

# =========================
# Header
# =========================
st.markdown(
    """
    <div style="
        padding: 18px;
        border-radius: 16px;
        border: 1px solid rgba(49,51,63,0.18);
    ">
        <div style="font-size:34px; font-weight:800;">
            📘 Introdução à Plataforma
        </div>
        <div style="margin-top:6px; font-size:16px; opacity:0.85;">
            Portal de Trilhas de Capacitação Técnica – Telecomunicações
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================
# Texto institucional
# =========================
st.markdown(
"""
A **Plataforma de Trilhas de Capacitação Técnica – Telecomunicações** foi desenvolvida com o objetivo de estruturar, acompanhar e evidenciar o desenvolvimento técnico e comportamental dos colaboradores do laboratório, alinhando as competências individuais às necessidades operacionais, regulatórias e estratégicas da área.

A ferramenta consolida, em ambiente único, as principais informações relacionadas à capacitação interna, permitindo visualizar de forma integrada:

- Trilhas de aprendizagem estruturadas por função e nível de complexidade  
- Conteúdos técnicos, normativos e tecnológicos aplicáveis às atividades laboratoriais  
- Formas de capacitação disponíveis, internas e externas  
- Tempo estimado de desenvolvimento por competência  
- Critérios objetivos de avaliação técnica  
- Observações relacionadas às particularidades e características de cada módulo  
- Cenário atual de aderência e maturidade técnica dos colaboradores  
"""
)

st.write("")

# =========================
# Finalidade estratégica
# =========================
st.markdown("## 🎯 Finalidade Estratégica")

st.markdown(
"""
Além de atuar como instrumento estruturado de gestão do conhecimento, a plataforma foi concebida como uma ferramenta de diagnóstico organizacional, permitindo mapear de forma clara o cenário atual de competências técnicas da equipe.

A partir dessa análise, torna-se possível:

- Identificar lacunas de conhecimento  
- Direcionar treinamentos de forma assertiva  
- Priorizar desenvolvimentos críticos para a operação  
- Planejar sucessões técnicas  
- Sustentar expansões de escopo e processos de acreditação  
"""
)

st.write("")

# =========================
# Contexto da vaga
# =========================
st.markdown("## 🧩 Contexto Estratégico – Desenvolvimento Interno")

st.markdown(
"""
Adicionalmente, a estruturação da trilha permite atuar de forma estratégica no desenvolvimento interno de competências, com o objetivo de formar profissionais aptos a atender demandas técnicas específicas da área, incluindo o fortalecimento do quadro frente à vaga atualmente aberta no laboratório.

A plataforma possibilita acelerar o desenvolvimento direcionado dos colaboradores, reduzindo gaps técnicos e ampliando a autonomia operacional da equipe.
"""
)

st.markdown(
"""
🔗 **Acesse a vaga:**  
https://pucrs.gupy.io/jobs/9629305?jobBoardSource=gupy_public_page
"""
)

st.write("")
st.divider()

st.caption(
    "Portal de Trilhas de Capacitação Técnica – Telecomunicações • "
    "Gestão de Competências • Desenvolvimento Interno • LABELO"
)
