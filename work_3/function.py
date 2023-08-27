
import json
from quest import *

def open_file(path):
    """
    Загружает список словарей из файла.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def questions_sem(path):
    """
    Создает список экземпляров.
    """
    load_file = open_file(path)
    questions = []
    for load_file_1 in load_file:
        word = load_file_1["q"]
        complexity = int(load_file_1["d"])
        response = load_file_1["a"]
        question = Question(word, complexity, response)
        questions.append(question)
    return questions

def statistics(path):
    """
    Выводит статистику.
    """
    point = 0
    count = 0
    for total in path:
        if total.is_correct():
            point += total.points
            count += 1
    return f'Вот и всё!\n'\
           f'Отвечено {count} вопроса из {len(path)}\n'\
           f'Набрано баллов: {point}'


