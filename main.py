import time
import requests
import json
from time_modul import time_now, date_now


def form_channel():
    # С0-30 до4-30 каждого дня оприделяет максимум и минимум и передает в price_breakout
    print('Зашли в form_channel')
    # time_mod_midnight()

    url = 'https://www.bitmex.com/api/v1/trade/bucketed?binSize=5m&partial=false&symbol=XBTUSD&columns=open%2C%20close%20%2Chigh%2C%20low%2C%20volume%2C%20trades&reverse=false&' \
          f'startTime={date_now()}%2001%3A30&endTime={date_now()}%2004%3A30'
    resp = requests.get(url).text
    data = json.loads(resp)
    print(data)


def price_breakout(min_price, max_price):
    # Функция следит за ценой и как только цена пересекает уровень, передает управление number_of_trades
    # ФУНКЦИЯ ПРОТЕСТИРОВАНА
    while True:
        url = 'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=price&count=1&reverse=true'
        resp = requests.get(url).text
        data = json.loads(resp)
        print(data[0]['price'])
        current_price = data[0]['price']
        if current_price > min_price and current_price < max_price:
            time.sleep(5)
        else:
            return number_of_trades()


def number_of_trades():
    # Считает количество сделок с начала той минуты, когда цена пробила уровень. Если больше 300-т,
    # то открываем сделку. Запросы будем отправлять каждые 5 секунд.
    # ФУНКЦИЯ ПРОТЕСТИРОВАНА.
    while True:
        url_trade = f'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=side%2C%20size%2C%20' \
                    f'price&count=1000&reverse=false&startTime={time_now()}'
        resp_trade = requests.get(url_trade).text
        data_trade = json.loads(resp_trade)
        print(f'Количество сделок :{len(data_trade)}')
        if len(data_trade) > 300:  # 300
            return ('Сделок больше 300-т Открываем ордер')
        else:
            time.sleep(10)


if __name__ == '__main__':
    price_breakout(min_price=20275, max_price=21000)
