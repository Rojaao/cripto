import streamlit as st
import pandas as pd
from arbitragem import buscar_oportunidades, coletar_precos_completos
import time

st.set_page_config(page_title="Arbitragem Cripto", layout="wide")
st.title("🔁 Robô de Arbitragem Cripto - Atualização Automática")

st.markdown("Monitoramento automático em tempo real das principais exchanges.")

# Pares comuns e líquidos nas exchanges Binance, Bybit, OKX, KuCoin, Gate.io
pares = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "XRP/USDT",
    "DOGE/USDT",
    "ADA/USDT",
    "SOL/USDT",
    "MATIC/USDT",
    "LTC/USDT",
    "DOT/USDT"
]

intervalo = st.slider("⏱️ Intervalo de atualização (segundos)", 5, 60, 10)

placeholder_precos = st.empty()
placeholder_oportunidades = st.empty()

def atualizar():
    df_precos = coletar_precos_completos(pares)
    df_oportunidades = buscar_oportunidades(pares)

    placeholder_precos.subheader("📊 Preços coletados por exchange e par")
    placeholder_precos.dataframe(df_precos)

    placeholder_oportunidades.subheader("💰 Oportunidades de arbitragem encontradas")
    if not df_oportunidades.empty:
        placeholder_oportunidades.dataframe(df_oportunidades.sort_values("lucro_percent", ascending=False), use_container_width=True)
    else:
        placeholder_oportunidades.warning("Nenhuma oportunidade de arbitragem encontrada no momento.")

while True:
    atualizar()
    time.sleep(intervalo)
