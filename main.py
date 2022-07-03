import requests
import json
import pandas as pd
from time_modul import time_now


def number_of_trades():
    # Считает количество сделок с начала той минуты, когда цена пробила уровень. Если болше 300-т то открываес сделку
    # Запросы будем отправлять каждые 5 секунд
    url_trade = f'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=side%2C%20size%2C%20price&count=1000&reverse=false&startTime={time_now()}'
    resp_trade = requests.get(url_trade).text
    data_trade = json.loads(resp_trade)
    print(f'Количество сделок :{len(data_trade)}')


def check_channel():
    pass


def write_file():
    url = 'https://www.bitmex.com/api/v1/trade/bucketed?binSize=1m&partial=false&symbol=XBTUSD&columns=open%2C%20close%20%2Chigh%2C%20low%2C%20volume%2C%20trades&count=800&reverse=false&startTime=2022-06-30%2000%3A30&endTime=2022-07-03%2006%3A40'
    url_trade = 'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=side%2C%20size%2C%20price&count=1000&reverse=false&startTime=2022-06-30%2006%3A16&endTime=2022-06-30%2006%3A25'
    # в url_trade время как в терминале. В trade на минуту больше
    resp = requests.get(url).text
    resp_trade = requests.get(url_trade).text
    data = json.loads(resp)
    data_trade = json.loads(resp_trade)

    df = pd.DataFrame(data)
    df.to_excel('stat.xlsx')
    df_trade = pd.DataFrame(data_trade)
    df_trade.to_excel('stat_trade.xlsx')


if __name__ == '__main__':
    number_of_trades()
