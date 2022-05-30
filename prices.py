# imports
import json

import requests


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
            rank = x["cmcRank"] if x["cmcRank"] else None
            name = x["name"] if x["name"] else None
            market_cap = x["quotes"][0]["marketCap"] if x["quotes"][0]["marketCap"] else None
            price = x["quotes"][0]["price"] if x["quotes"][0]["price"] else None

            circulating_supply = x["circulatingSupply"] if x["circulatingSupply"] else None
            volume_24h = x["quotes"][0]["volume24h"] if x["quotes"][0]["volume24h"] else None

            percent_change_1h = str(round(x["quotes"][0]["percentChange1h"], 2)) + "%" if x["quotes"][0][
                "percentChange1h"] else None
            percent_change_24h = str(round(x["quotes"][0]["percentChange24h"], 2)) + "%" if x["quotes"][0][
                "percentChange24h"] else None
            percent_change_7d = str(round(x["quotes"][0]["percentChange7d"], 2)) + "%" if x["quotes"][0][
                "percentChange7d"] else None
            return price, percent_change_1h


if __name__ == "__main__":
    price, percent_change_1h = crypto_parser(symbol="GENE")

    print(price)