"""
Word Occurrences Counter
Estimate: 20 minutes
Actual:   15 minutes
"""

from operator import itemgetter

word_to_count = {}
word_count = 0
word_length = 0

text = input("Enter text: ").split()
text = sorted(text)

print(text)

for word in text:
    word_count = text.count(word)
    word_to_count[word] = word_count

print(word_to_count)

word_to_count = sorted(word_to_count.items(), key=itemgetter(0, 1))
word_to_count = dict(word_to_count)
print(word_to_count)

for word in word_to_count:
    if len(word) > word_length:
        word_length = len(word)

for word, count in word_to_count.items():
    print(f"{word:<{word_length}} : {count}")