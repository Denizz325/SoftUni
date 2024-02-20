random_words = input().split()
word_dict = {}

for word in random_words:
    lower_word = word.lower()

    if lower_word not in word_dict:
        word_dict[lower_word] = 0
    word_dict[lower_word] += 1

for word, count in word_dict.items():
    if count % 2 != 0:
        print(word, end=" " )
