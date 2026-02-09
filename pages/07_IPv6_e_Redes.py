import streamlit as st

st.set_page_config(
    page_title="IPv6 & Redes",
    page_icon="🌐",
    layout="wide"
)

# ======================
# Header profissional
# ======================
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        7️⃣ IPv6 & Redes
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Desenvolvimento de domínio técnico para configuração de rede, montagem de topologias de teste
        e execução de ensaios relacionados a IPv6 (incluindo leitura e interpretação de normas e RFCs).
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
    card("🎚️ Nível de dificuldade", "Difícil")

with c3:
    card("🎓 Modalidade", "Cursos + leitura<br>orientada + prática")

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
- RFC 8200  
- IPv6 Ready  
- ICMPv6 e NDP  
- Topologia de testes  
- Configuração de rede para ensaios  
        """
    )

with tab2:
    st.subheader("🎓 Formas de Aprendizado")

    st.markdown("**Cursos (online / presencial):**")
    st.markdown(
        """
- ✅ **Grátis (EAD) — conforme agenda** — [NIC.br: Curso Básico IPv6 (EAD)](https://cursoseventos.nic.br/curso/curso-basico-ipv6-ead/)  
- ✅ **Grátis (presencial) — conforme agenda** — [IPv6.br: Curso Avançado Presencial](https://ipv6.br/pagina/curso-avancado-presencial/)  
- ✅ **Grátis (online)** — [Hurricane Electric: IPv6 Certification](https://ipv6.he.net/certification/)  
        """
    )

    st.markdown("**Complemento técnico (interno):**")
    st.markdown(
        """
- Aulas teóricas sobre fundamentos do protocolo IPv6  
- Leitura orientada da RFC 8200 e documentos complementares  
- Estudo das diferenças entre IPv4 e IPv6  
        """
    )

with tab3:
    st.subheader("✅ Avaliação")
    st.markdown(
        """
- Configurar rede para ensaio  
- Validar topologia IPv6  
- Executar testes de IPv6  
        """
    )

with tab4:
    st.subheader("📝 Observações")
    st.write(
        "A maior parte dos cursos e documentações disponíveis sobre IPv6 está direcionada à implementação e adaptação de serviços e "
        "infraestruturas — como sites, redes corporativas e provedores — com foco em utilização e implantação do protocolo."
    )
    st.write(
        "Entretanto, há limitada oferta de conteúdos voltados especificamente à execução de ensaios laboratoriais e avaliação de conformidade. "
        "Dessa forma, o tema exige elevado nível de domínio técnico por parte do profissional, especialmente para interpretação de requisitos, "
        "montagem de topologias de teste e condução adequada dos ensaios."
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
