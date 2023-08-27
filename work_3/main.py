
import random
from function import *

questions_json = 'questions.json'
questions_py = questions_sem(questions_json)

random.shuffle(questions_py)
for quest_temp in questions_py:
    print(quest_temp.build_question())
    user_input = input("Ваш ответ: ")

    quest_temp.user = user_input
    print(quest_temp.build_feedback())

print(statistics(questions_py))






