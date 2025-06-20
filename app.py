import streamlit as st
import pandas as pd
from arbitragem import buscar_oportunidades, coletar_precos_completos

st.set_page_config(page_title="Arbitragem Cripto", layout="wide")
st.title("🔁 Robô de Arbitragem Cripto - Modo Simulação")

st.markdown("Monitora preços em tempo real nas principais exchanges e mostra oportunidades de arbitragem.")

# Pares comuns suportados nas exchanges principais
pares = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "XRP/USDT",
    "DOGE/USDT"
]

intervalo = st.slider("⏱️ Intervalo de atualização (segundos)", 5, 60, 10)

if st.button("🔍 Buscar oportunidades agora"):
    df_oportunidades = buscar_oportunidades(pares)
    df_precos = coletar_precos_completos(pares)

    st.subheader("📊 Preços coletados por exchange e par")
    st.dataframe(df_precos)

    st.subheader("💰 Oportunidades de arbitragem encontradas")
    if not df_oportunidades.empty:
        st.dataframe(df_oportunidades.sort_values("lucro_percent", ascending=False), use_container_width=True)
    else:
        st.warning("Nenhuma oportunidade de arbitragem encontrada no momento.")
else:
    st.info("Clique em 'Buscar oportunidades agora' para iniciar a análise.")
