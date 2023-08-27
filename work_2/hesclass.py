
class BasicWord:
    def __init__(self, original_word, subwords):
        self.original_word = original_word
        self.subwords = subwords

    def check_subword(self, subwords):
        return subwords in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f"BasicWord(word={self.original_word}, subwords={self.subwords})"

#print(BasicWord("питон", ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"]))

class Player:

    def __init__(self, username):
        self.username = username
        self.word_used = []

    def user_word(self):
        return len(self.word_used)

    def used_word(self, word):
        self.used_word.append(word)

    def check_word(self, word):
        return word in self.used_word

    def __repr__(self):
        return f"Player(username={self.username})"
