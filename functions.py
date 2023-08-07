import random


def len_words_from_file(path):
    """
     Функция читающая список слов.
    :param path: Путь до файла.
    :return: Возвращает слово.
    """
    with open(path, 'r', encoding='utf8') as file:
       words = file.read().strip().split("\n")
    return words


def shuffle_word(word):
    """
    Функция перемешивающая слова.
    :param word: Слово которое перемешиваем.
    :return: Возвращает перемешаное слово.
    """
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def record_player(path, player_name, player_count):
    """
    Функция записи игрока в файл.
    :param path: Путь до файла.
    :param player_name: Имя игрока.
    :param player_count: Очки игрока.
    :return: None.
    """
    with open(path, 'a', encoding='utf8') as file:
        file.write(f'{player_name}  {player_count} \n')


def read_history(path):
    """
    Функция записи данныйх в файл.
    :param path: Путь к файлу.
    :return: Возвращает количество игр и макс рекород по ним.
    """
    max = 0
    count = 0

    with open(path, "r", encoding="utf8") as file:
        for line in file.readlines():
            count += 1
            score = int(line.split("  ")[1])

            if score > max:
                max = score

    return f"Всего игр сыграно: {count}\n" \
           f"Максимальный рекорд: {max}"
