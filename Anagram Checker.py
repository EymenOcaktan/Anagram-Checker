word = input("Enter a word: ")
word = word.lower()
sorted_word = sorted(word)
word2 = input("Enter another word: ")
word2 = word2.lower()
sorted_word2 = sorted(word2)
if sorted_word == sorted_word2:
    print(f"{word} and {word2} are anagrams")
else:
    print(f"{word} and {word2} are not anagrams")