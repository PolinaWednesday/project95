
from utils import *
from hesclass import *

user_name = input("Ввведите имя игрока ")

player = Player(user_name)

url_name = "https://www.jsonkeeper.com/b/LTJB"
random_word = load_random_word(url_name)

print(f"Привет {user_name}")
print(f"Составьте {len(random_word.subwords)} слов из слова {random_word.original_word.upper()}\n"
      f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
      f"Поехали, ваше первое слово?")

while





