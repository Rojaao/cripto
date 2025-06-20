
import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

st.set_page_config(page_title='Robô Cripto Avançado', layout='wide')
st.title("Painel Robô Cripto - BTC, ETH, BNB (Simulação R$50)")

# Sidebar config
st.sidebar.header("Configurações")
valor_operacao = st.sidebar.number_input("Valor por operação (R$)", value=50)
num_trades = st.sidebar.slider("Número de operações simuladas", 10, 100, 20)
ativos = ["BTC", "ETH", "BNB"]
st.sidebar.write("Ativos analisados:", ", ".join(ativos))

# Simulação de operações
st.subheader("📈 Operações Simuladas")
dados = []
agora = datetime.now()
for i in range(num_trades):
    ativo = random.choice(ativos)
    direcao = random.choice(["Compra", "Venda"])
    preco_entrada = round(random.uniform(100, 1000), 2)
    preco_saida = preco_entrada + round(random.uniform(-20, 30), 2)
    resultado = round((preco_saida - preco_entrada) if direcao == "Compra" else (preco_entrada - preco_saida), 2)
    lucro_prejuizo = round((resultado / preco_entrada) * valor_operacao, 2)
    hora = (agora - timedelta(minutes=i)).strftime('%H:%M:%S')
    dados.append([hora, ativo, direcao, preco_entrada, preco_saida, f"R$ {lucro_prejuizo}"])

df = pd.DataFrame(dados, columns=["Hora", "Ativo", "Direção", "Entrada", "Saída", "Resultado (R$)"])
st.dataframe(df, use_container_width=True)

# Métricas de desempenho
st.subheader("📊 Resumo de Performance")
resultados_float = df["Resultado (R$)"].apply(lambda x: float(x.replace("R$", "").strip()))
lucro_total = resultados_float[resultados_float > 0].sum()
prejuizo_total = resultados_float[resultados_float < 0].sum()
total = resultados_float.sum()
taxa_acerto = (resultados_float[resultados_float > 0].count() / len(resultados_float)) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Lucro Total", f"R$ {round(lucro_total, 2)}")
col2.metric("📉 Prejuízo Total", f"R$ {round(prejuizo_total, 2)}")
col3.metric("📊 Resultado Final", f"R$ {round(total, 2)}")
col4.metric("🎯 Taxa de Acerto", f"{round(taxa_acerto, 2)}%")
