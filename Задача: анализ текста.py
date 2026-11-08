answer = input("Введите текст: ").lower()
text = answer.split(" ")
count_text = len(text)
words_count = {}
for word in text:
    if word in words_count:
        words_count[word] = words_count[word] + 1
    else:
        words_count[word] = 1
most_words = ""
most_count = 0
for word, count in words_count.items():
    if count > most_count:
        most_count = count
        most_words = word

print(words_count)
print(most_words, most_count)