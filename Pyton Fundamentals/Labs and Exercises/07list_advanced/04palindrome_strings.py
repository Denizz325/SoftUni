words = input().split()
palindrome_word = input()

palindrome_words_list = []
palindrome_word_count = 0

for word in words:
    if word == word[::-1]:
        palindrome_words_list.append(word)

palindrome_word_count += palindrome_words_list.count(palindrome_word)

print(palindrome_words_list)
print(f"Found palindrome {palindrome_word_count} times")