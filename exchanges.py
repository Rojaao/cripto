import ccxt

# Instância das exchanges públicas via CCXT
exchanges = {
    "Binance": ccxt.binance(),
    "Bybit": ccxt.bybit(),
    "OKX": ccxt.okx(),
    "KuCoin": ccxt.kucoin(),
    "Gate.io": ccxt.gateio(),
}

def obter_preco(exchange, par):
    try:
        book = exchange.fetch_order_book(par)
        return book['ask'][0], book['bid'][0]  # ask (compra), bid (venda)
    except:
        return None, None