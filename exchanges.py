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
        ask = book['asks'][0] if book['asks'] else None
        bid = book['bids'][0] if book['bids'] else None
        if ask is None or bid is None:
            print(f"[LOG] Ordem de compra (ask) ou venda (bid) vazia para {par} na {exchange.name}")
        return ask, bid
    except Exception as e:
        print(f"[ERRO] Não foi possível obter preço para {par} na {exchange.name}: {e}")
        return None, None
