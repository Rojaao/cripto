from exchanges import exchanges, obter_preco
import pandas as pd

# Taxa média estimada por transação (0.1%)
TAXA = 0.001

def buscar_oportunidades(pares):
    resultados = []

    for par in pares:
        precos = {}
        for nome, ex in exchanges.items():
            ask, bid = obter_preco(ex, par)
            if ask and bid:
                precos[nome] = {"ask": ask, "bid": bid}

        for ex_compra in precos:
            for ex_venda in precos:
                if ex_compra != ex_venda:
                    preco_compra = precos[ex_compra]["ask"]
                    preco_venda = precos[ex_venda]["bid"]
                    lucro_bruto = preco_venda - preco_compra
                    lucro_percent = (lucro_bruto / preco_compra - 2*TAXA) * 100

                    if lucro_percent > 0:
                        resultados.append({
                            "par": par,
                            "compra_em": ex_compra,
                            "venda_em": ex_venda,
                            "preco_compra": round(preco_compra, 4),
                            "preco_venda": round(preco_venda, 4),
                            "lucro_percent": round(lucro_percent, 2)
                        })

    return pd.DataFrame(resultados)