
class BasicWord:
    def __init__(self, original_word, subwords):
        self.original_word = original_word
        self.subwords = subwords
        self.used_subwords = []


    def add_used_subword(self, subword):
        """
        Добавляет использованные подслова.
        """
        self.used_subwords.append(subword)


    def check_subword(self, subword):
        """
        Проверку введенного слова в списке допустимых подслов.
        """
        return subword in self.subwords


    def count_subwords(self):
        """
        Подсчет количества подслов.
        """
        return self.used_subwords


    def __repr__(self):
        return f"BasicWord(word={self.original_word}, subwords={self.subwords})"


class Player:

    def __init__(self, username):
        self.username = username
        self.word_used = []


    def user_word(self):
        """
        Получение количества использованных слов.
        """
        return len(self.word_used)


    def used_word(self, word):
        """
        Добавление слова в использованные слова.
        """
        self.word_used.append(word)


    def check_word(self, word):
        """
        Проверка использования данного слова до этого.
        """
        return word in self.word_used


    def __repr__(self):
        return f"Player(username={self.username})"

