
import random
import requests
import urllib3
from hesclass import *


def load_random_word(url):
    """
    Получит список слов с внешнего ресурса,
    выберет случайное слово,
    создаст экземпляр класса BasicWord,
    вернет этот экземпляр.
    :param url: Адрес внешнего ресурса.
    :return: Экземпляр класса.
    """
    urllib3.disable_warnings() # не понимаю что это
    response = requests.get(url=url, verify=False) # достает данные из сайта
    random_word = random.choice(response.json()) # выберет случайное слово
    if response.status_code == 200: # проверка статус кода (200 = ОК)
        instance = BasicWord(random_word["word"], random_word["subwords"])  # создаст экземпляр класса BasicWord
        return instance
