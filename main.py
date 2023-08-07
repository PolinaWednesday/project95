from functions import len_words_from_file, shuffle_word, record_player, read_history


words_txt = 'words.txt'
history_txt = 'history.txt'
words = len_words_from_file('words.txt')
user_name = input("Введите ваше имя: ")
count = 0
for word in words:
    shuffle_word(word)
    user_answer = input(f'Угадайте слово: {shuffle_word(word)} ')
    if user_answer.lower().strip(" ") == word:
        print(f"Верный ответ! Вы получаете: 10 балов")
        count += 10
    else:
        print(f"Неверно! Верный ответ – {word}")

record_player(history_txt, user_name, count)
print(read_history(history_txt))
