import json
import os


def load_students(path: str) ->dict:
    """
    Загружает студентов.
    :param path: Путь до файла.
    :return: Возвращает данные студента.
    """

    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_professions(path: str) ->dict:
    """
    Загружает профессии.
    :param path: Путь до файла.
    :return: Возвращает данные о профессии
    """

    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_student_by_pk(pk: int) ->dict:
    """
    Из списков студентов достает нужных по pk.
    :param pk: Данные из функции load_students.
    :return: Возвращает номер студента.
    """

    all_students = load_students("students.json")
    for student in all_students:
        if student['pk'] == pk:
            return student


def get_profession_by_title(title: str) ->dict:
    """
    Из списка профессий достает нужную по ее названию.
    :param title: Данные из функции load_professions.
    :return: Возвращает название профессии.
    """

    all_professions = load_professions("professions.json")
    for one_profe in all_professions:
        if one_profe["title"] == title:
            return one_profe


def check_fitness(student, professions: str) -> dict:
    """
    Получает данные студента и профессии.
    :param student: Данные из функции get_student_by_pk
    :param professions: Данные из функции get_profession_by_title.
    :return: Словарь c данными о соответствии студента.
    """

    set_students = set(student["skills"])
    set_professions = set(professions["skills"])
    has_skills = set_students.intersection(set_professions)
    lacks_skills = set_professions.difference(set_students)
    fit_percent = round(len(has_skills) / len(lacks_skills) * 100)
    dict_resalt = {
        "has": has_skills,
        "lacks": lacks_skills,
        "fit_percent": fit_percent
    }
    return dict_resalt


def show_result(data, name):
    """
    Выводит данные студента и профессии.
    :param data: Данные из функции check_fitness.
    :param name: Имя студента из списка.
    :return: Вывод информации о соответствии студентов.
    """
    str_has = ", ".join(data['has'])
    str_lacks = ", ".join(data['lacks'])
    str_output = f'Пригодность {data["fit_percent"]}\n' \
                 f'{name} знает {str_has}\n' \
                 f'{name} не занет {str_lacks}\n'
    return str_output
