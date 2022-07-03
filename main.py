import requests
import json
import pandas as pd


def check_channel():
    c = 1000
    url = f'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=side%2C%20price%2C%20size%2C%20tickDirection&count={c}&reverse=true'
    resp = requests.get(url).text
    data = json.loads(resp)
    i = c - 1
    while i > 0:
        print(data[i])
        i -= 1
    else:
        df = pd.DataFrame(data)
        df.to_excel('stat.xlsx')


if __name__ == '__main__':
    check_channel()
