import streamlit as st
import pandas as pd
from arbitragem import buscar_oportunidades

st.set_page_config(page_title="Arbitragem Cripto", layout="wide")
st.title("🔁 Robô de Arbitragem Cripto - Modo Simulação")

st.markdown("Monitora preços em tempo real nas principais exchanges e mostra oportunidades de arbitragem.")

pares = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "DOGE/USDT", "SHIB/USDT"]
intervalo = st.slider("⏱️ Intervalo de atualização (segundos)", 5, 60, 10)

if st.button("🔍 Buscar oportunidades agora"):
    df = buscar_oportunidades(pares)
    if not df.empty:
        st.dataframe(df.sort_values("lucro_percent", ascending=False), use_container_width=True)
    else:
        st.warning("Nenhuma oportunidade de arbitragem encontrada no momento. Verifique pares ou conexão com exchanges.")
else:
    st.info("Clique em 'Buscar oportunidades agora' para iniciar a análise.")