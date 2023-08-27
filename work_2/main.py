
from utils import *
from hesclass import *

#Ввод имени
user_name = input("Ввведите имя игрока ")

player = Player(user_name)
#Ссылка на слова
url_name = "https://www.jsonkeeper.com/b/LTJB"
random_word = load_random_word(url_name)

print(f"Привет {user_name}")
print(f"Составьте {len(random_word.subwords)} слов из слова {random_word.original_word.upper()}\n"
      f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
      f"Поехали, ваше первое слово?")

#Цикл для слов
while True:

    word = input().lower()

    if word == "stop" or word == "стоп":
        break
    else:
        # Если слово короче 3 букв, выводим сообщение об ошибке
        if len(word) < 3:
            print("Слишком короткое слово")
            continue

        # Если введенное слово не является допустимым подсловом, выводим сообщение об ошибке
        if not random_word.check_subword(word):
            print(f"Неверно")
            continue

        # Если слово уже использовано, выводим сообщение об ошибке
        if player.check_word(word):
            print("Уже использовано")
            continue

        # Добавляем использованное подслово в случайное слово и использованное слово в список использованных слов игрока.
        random_word.add_used_subword(word)
        player.used_word(word)
        print(f"Верно!")

    # Если все подслова случайного слова были угаданы, то игра завершается.
    if len(random_word.count_subwords()) == len(random_word.subwords):
        break

print(f"Игра завершена, вы угадали {player.user_word()} слов!")
