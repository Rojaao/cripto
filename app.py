
import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title='Robô Cripto', layout='wide')
st.title("Painel Robô Cripto - BTC, ETH, BNB")

st.sidebar.header("Configuração")
valor_operacao = st.sidebar.number_input("Valor por operação (R$)", value=50)

ativos = ["BTC", "ETH", "BNB"]
st.sidebar.write("Ativos analisados:", ", ".join(ativos))

st.subheader("Simulação de Trades (R$50 cada)")
dados = []
for i in range(10):
    ativo = random.choice(ativos)
    direcao = random.choice(["Compra", "Venda"])
    resultado = round(random.uniform(-10, 20), 2)
    dados.append([ativo, direcao, f"R$ {valor_operacao}", f"R$ {resultado}"])

df = pd.DataFrame(dados, columns=["Ativo", "Direção", "Valor Operado", "Resultado"])
st.dataframe(df, use_container_width=True)

st.subheader("Resumo")
total = df["Resultado"].apply(lambda x: float(x.replace("R$", "").strip())).sum()
st.metric("Lucro/Prejuízo Total", f"R$ {round(total, 2)}")
