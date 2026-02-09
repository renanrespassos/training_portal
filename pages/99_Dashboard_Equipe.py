import streamlit as st
import pandas as pd

st.set_page_config(page_title="Técnicos Internos", page_icon="👥", layout="wide")

# -----------------------------
# Dados (fácil de editar)
# -----------------------------
MODULES = [
    "1 Fundamentos de Metrologia em Radio Frequência",
    "2 Tecnologias de Comunicação Sem Fio",
    "3 Configuração de Amostras",
    "4 Qualidade ISO IEC17025:2017",
    "5 Regulatório Anatel",
    "6 Ensaios em Estações Terminais de Acesso (ETA)",
    "7 IPv6 & Redes",
    "8 Soft Skills",
]

TEAM = {
    "Bernardo": {
        "cargo": "Assistente de Laboratório",
        "formacao": "Curso técnico em Eletrônica (completo)",
        "scores": {
            MODULES[0]: (70, "Desenvolvimento"),
            MODULES[1]: (60, "Desenvolvimento"),
            MODULES[2]: (60, "OK"),
            MODULES[3]: (60, "Desenvolvimento"),
            MODULES[4]: (50, "Desenvolvimento"),
            MODULES[5]: (0, "OK"),
            MODULES[6]: (0, "OK"),
            MODULES[7]: (40, "Desenvolvimento - Foco"),
        },
        "obs": (
            "Bernardo está sendo treinado principalmente para ser a referência para os ensaios do Ato 14448 "
            "e também o organizador do cronograma e da equipe. "
            "Ele cuida principalmente dos ensaios com maior demanda e dos processos mais básicos."
        ),
    },

    "Eduardo": {
        "cargo": "Analista de Laboratório",
        "formacao": "Técnico em Eletrônica (completo) • Engenharia em andamento",
        "scores": {
            MODULES[0]: (90, "OK"),
            MODULES[1]: (80, "OK"),
            MODULES[2]: (90, "OK"),
            MODULES[3]: (30, "Desenvolvimento"),
            MODULES[4]: (70, "Desenvolvimento - Foco"),
            MODULES[5]: (80, "Desenvolvimento - Foco"),
            MODULES[6]: (80, "Desenvolvimento"),
            MODULES[7]: (20, "Desenvolvimento"),
        },
        "obs": (
            "Eduardo está à frente dos ensaios mais complexos envolvendo redes móveis. "
            "É responsável pelo desenvolvimento de alguns métodos e atua como signatário da área. "
            "Será responsável pelas pesquisas e ensaios de 5G."
        ),
    },

    "Joao Pinheiro": {
        "cargo": "Analista de Laboratório",
        "formacao": "Técnico em Eletrônica (completo) • Engenharia Mecatrônica em andamento",
        "scores": {
            MODULES[0]: (90, "OK"),
            MODULES[1]: (90, "OK"),
            MODULES[2]: (90, "OK"),
            MODULES[3]: (40, "Desenvolvimento"),
            MODULES[4]: (30, "Desenvolvimento - Foco"),
            MODULES[5]: (0, "OK"),
            MODULES[6]: (30, "OK"),
            MODULES[7]: (20, "Desenvolvimento"),
        },
        "obs": (
            "João está à frente de outros tipos de ensaios que envolvem métodos presentes em nosso escopo "
            "e que exigem maior nível de experiência para execução. Além disso, atua em melhorias internas do laboratório."
        ),
    },

    "Greter": {
        "cargo": "Analista de Laboratório",
        "formacao": "Engenharia (concluída)",
        "scores": {
            MODULES[0]: (20, "OK"),
            MODULES[1]: (20, "OK"),
            MODULES[2]: (20, "OK"),
            MODULES[3]: (20, "Desenvolvimento"),
            MODULES[4]: (30, "Desenvolvimento - Foco"),
            MODULES[5]: (50, "Desenvolvimento - Foco"),
            MODULES[6]: (50, "Desenvolvimento"),
            MODULES[7]: (20, "Desenvolvimento"),
        },
        "obs": (
            "Greter executa os testes mais complexos com supervisão do Eduardo (maior senioridade técnica). "
            "Será responsável pelos ensaios atuais e irá ensinar a Lauren em um futuro próximo."
        ),
    },

    "Lauren": {
        "cargo": "Assistente de Laboratório",
        "formacao": "Vinda da calibração (experiência prática forte)",
        "scores": {
            MODULES[0]: (80, "OK"),
            MODULES[1]: (0, "OK"),
            MODULES[2]: (0, "OK"),
            MODULES[3]: (50, "OK"),
            MODULES[4]: (0, "Desenvolvimento - Foco"),
            MODULES[5]: (0, "Desenvolvimento - Foco"),
            MODULES[6]: (0, "Desenvolvimento - Foco"),
            MODULES[7]: (0, "OK"),
        },
        "obs": (
            "Lauren irá vir da calibração para aprender a executar os ensaios de ETA e IPv6 em um primeiro momento, "
            "devido ao desempenho entregue na calibração."
        ),
    },
}

# -----------------------------
# Helpers
# -----------------------------
def status_badge(score: int, status: str) -> str:
    # remove "OK" abaixo de 50% (e, na prática, qualquer status abaixo de 50% pode ficar vazio)
    if score < 50 and status.strip().lower() == "ok":
        return ""
    if score < 50 and status.strip() == "":
        return ""
    if score < 50 and status.strip().lower() == "ok":
        return ""
    if score < 50 and status.strip().lower() != "ok":
        # mantém Desenvolvimento/Foco se você quiser (mas você pediu só tirar OK)
        return status
    # score >= 50
    if status.strip().lower() == "ok":
        return "OK"
    return status


def make_individual_df(name: str) -> pd.DataFrame:
    p = TEAM[name]
    rows = []
    for m in MODULES:
        score, status = p["scores"].get(m, (0, "OK"))
        rows.append({
            "Módulo": m,
            "Adesão (%)": int(score),
            "Status": status_badge(int(score), str(status)),
        })
    return pd.DataFrame(rows)


def make_overall_df() -> pd.DataFrame:
    rows = []
    for person in TEAM.keys():
        p = TEAM[person]
        scores = [p["scores"].get(m, (0, ""))[0] for m in MODULES]
        avg = sum(scores) / len(scores)
        rows.append({
            "Técnico": person,
            "Cargo": p["cargo"],
            "Média (%)": round(avg, 1),
        })
    return pd.DataFrame(rows).sort_values("Média (%)", ascending=False)


# -----------------------------
# UI
# -----------------------------
st.markdown(
    """
    <div style="padding: 16px 18px; border-radius: 16px; border: 1px solid rgba(49,51,63,0.18);">
      <div style="font-size: 34px; font-weight: 800; line-height: 1.15;">
        👥 Técnicos Internos — Aderência por Módulo
      </div>
      <div style="margin-top: 6px; font-size: 16px; opacity: 0.85;">
        Visão de desempenho por colaborador com indicadores de progresso, status e observações.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")

left, right = st.columns([1.2, 2.3], gap="large")

with left:
    person = st.selectbox("Selecione o técnico", list(TEAM.keys()))
    st.write("")
    st.markdown("#### Perfil")
    st.write(f"**Cargo:** {TEAM[person]['cargo']}")
    st.write(f"**Formação:** {TEAM[person]['formacao']}")

    st.write("")
    st.markdown("#### Observação")
    st.info(TEAM[person]["obs"])

with right:
    df = make_individual_df(person)

    avg = df["Adesão (%)"].mean()
    st.markdown("#### Visão geral do técnico selecionado")
    st.metric("Média de aderência", f"{avg:.1f}%")

    st.write("")
    st.markdown("#### Aderência por módulo")

    for _, r in df.iterrows():
        col_a, col_b = st.columns([3, 1.2])
        with col_a:
            st.write(r["Módulo"])
            st.progress(int(r["Adesão (%)"]))
        with col_b:
            st.write("")
            st.write(f"**{r['Adesão (%)']}%**")
            # só mostra status se existir
            if str(r["Status"]).strip():
                st.caption(r["Status"])

    st.write("")
    st.divider()

    st.markdown("#### Detalhamento (tabela)")
    st.dataframe(df, use_container_width=True, hide_index=True)

st.write("")
st.divider()

st.markdown("### Comparativo do time (média por técnico)")
overall = make_overall_df()
st.dataframe(overall, use_container_width=True, hide_index=True)

st.markdown("### Visualização (barras)")
chart_df = overall.set_index("Técnico")[["Média (%)"]]
st.bar_chart(chart_df)
