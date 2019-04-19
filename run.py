import sys
from collections import Counter

scrabble_rack = ''

try:
    scrabble_rack = str.lower(sys.argv[1])
except IndexError:
    print("please provide a 'scrabble rack' as argument")

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

file = open("sowpods.txt")
all_words = file.read().splitlines()
# print(all_words)
word_scores = {}

for word in all_words:
    score = 0
    temp_list = list(scrabble_rack)
    flag = 1
    for char in word:
        if str.lower(char) in temp_list:
            temp_list.remove(str.lower(char))
        else:
            flag = 0

    if flag == 1:
        dict_word = Counter(word)
        for key, value in dict_word.items():
            score += (scores[str.lower(key)] * value)
        word_scores.setdefault(score, []).append(word)

for key, value in reversed(sorted(word_scores.items())):
    for word in value:
        print key, word
