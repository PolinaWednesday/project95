from functions import *


def main():

    student_pk = input('Введите номер студента ')
    student = get_student_by_pk(int(student_pk))

    if student is None:
        print("У нас нет такого студента")
        quit()
    print(f'{student["full_name"]}\n'
          f'Знает {", ".join(student["skills"])}')

    profession_title = input(f'Выберите специальность для оценки студента {student["full_name"]} ')
    professions = get_profession_by_title(profession_title)

    if professions is None:
        print("У нас нет такой специальности")
        quit()

    fitness = check_fitness(student, professions)
    print(show_result(fitness, student['full_name']))


if __name__ == '__main__':
        main()
