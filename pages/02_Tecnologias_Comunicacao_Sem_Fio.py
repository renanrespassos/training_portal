import streamlit as st

st.set_page_config(
    page_title="Tecnologias de Comunicação Sem Fio",
    page_icon="📶",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        2️⃣ Tecnologias de Comunicação Sem Fio
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Base teórica sobre tecnologias sem fio utilizadas nos ensaios laboratoriais, com foco em especificações, cenários de aplicação e parâmetros típicos de configuração.
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
    card("🎚️ Nível de dificuldade", "Fácil")

with c3:
    card("🎓 Modalidade", "E-learning +<br>estudo guiado")

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
- Wi-Fi (IEEE 802.11)  
- Bluetooth  
- LoRa  
- ZigBee  
- Comunicação IoT  
- Redes Móveis (2G, 3G, 4G)  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Cursos (online):**")
    st.markdown(
        """
- ✅ **Grátis** — [Networking Basics (Cisco NetAcad)](https://www.netacad.com/courses/networking-basics?courseLang=en-US)  
- ✅ **Grátis** — [Networking Essentials (Cisco NetAcad)](https://www.netacad.com/courses/networking-essentials?courseLang=pt-BR)  
- ✅ **Grátis** — [Wi-Fi Fundamentals (Nordic Semiconductor Academy)](https://academy.nordicsemi.com/courses/wi-fi-fundamentals/)  
- ✅ **Grátis** — [Bluetooth Low Energy Fundamentals (Nordic Semiconductor Academy)](https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/)  
        """
    )

    st.markdown("**Complemento sugerido:**")
    st.markdown(
        """
- Leitura de documentações técnicas, manuais e guias de implementação (conforme demanda do projeto)  
- Estudo dirigido com apoio de ferramentas de IA para análise de características, limitações e parâmetros de configuração  
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
        "Conhecimento teórico sobre as principais tecnologias de comunicação sem fio utilizadas nos ensaios laboratoriais, "
        "compreendendo suas especificações técnicas, cenários de aplicação e requisitos de integração."
    )
    st.write(
        "Há grande volume de material disponível online — como documentações técnicas, manuais e guias de implementação — "
        "que pode ser consultado, inclusive com o auxílio de ferramentas de inteligência artificial, para suporte na análise "
        "de características, limitações e parâmetros de configuração."
    )
    st.write("**Status:** avaliando os demais cursos para complementar a trilha.")

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
