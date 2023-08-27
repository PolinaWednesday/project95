
class Question:
    def __init__(self, word, complexity, response):
        self.word = word
        self.complexity = complexity
        self.response = response
        self.points = self.complexity * 10
        self.user = None
        self.question = False

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points
    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.user == self.response


    def build_question(self):
        """
        Возвращает вопрос и сложность.
        """
        return f'Вопрос: {self.word}\nСложность {self.complexity}/5'


    def build_feedback(self):
        """
        Возвращает верный и не верный ответ.
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.response}'








