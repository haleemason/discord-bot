import json
from datetime import datetime, timedelta
import requests


def coinbase_price_check(sym="SOL-USD"):
    api_url = "https://api.pro.coinbase.com"
    bar_size = "900"

    delta = timedelta(minutes=15)
    time_end = datetime.now()
    time_start = time_end - (300 * delta)

    time_start = time_start.isoformat()
    time_end = time_end.isoformat()

    parameters = {"start": time_start, "end": time_end, "granularity": bar_size}
    # ["time","low","high","open","close","volume"]
    data = requests.get(
        f"{api_url}/products/{sym}/candles",
        params=parameters,
        headers={"content-type": "application/json"},
    )
    print(data.text)


def ftx_price_check(symbol: str) -> dict:
    """
    Simple function to check the price of a Cryptocurrency token by passing in its symbol.

    :param symbol: The abbreviated name of a cryptocurrency's coin or token for trading purposes,
     which is similar to a stock symbol on the stock market.
    :return: A dictionary of crypto price results from the FTX API
    """
    api_url = "https://ftx.com/api/markets"

    data = requests.get(f"{api_url}/{symbol}/USD", headers={"content-type": "application/json"})
    print(data.text)
    return data.json()["result"]


def crypto_parser(symbol: str):
    r = requests.get(
        "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all",
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        },
    )
    json_data = json.loads(r.text)
    for x in json_data["data"]["cryptoCurrencyList"]:
        if x["symbol"] == symbol:
            price = x["quotes"][0]["price"] if x["quotes"][0]["price"] else None
            percent_change_24h = (
                x["quotes"][0]["percentChange24h"] if x["quotes"][0]["percentChange24h"] else None
            )
            trend_24h_direction = "↗" if percent_change_24h >= 0 else "↘"
            percent_change_24h_formatted = f"({trend_24h_direction}{round(percent_change_24h, 2)}%)"
            return price, percent_change_24h_formatted


if __name__ == "__main__":
    symbol = "GENE"
    price, percent_change_24h = crypto_parser(symbol=symbol)
    print(f"{symbol}: ${round(price,2)} {percent_change_24h}")

    last_GENE_price = ftx_price_check(symbol="GENE")["last"]
    print(last_GENE_price)