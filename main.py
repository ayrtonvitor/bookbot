import os

path = os.path.abspath(__file__)
path = os.path.dirname(path)
path = os.path.join(path, "books/frankenstein.txt")

word_count = 0
letters_count = {}
with open(path, 'r') as f:
    for line in f:
        word_count += len(line.split())
        for w in line:
            letters_count[w.lower()] = letters_count.get(w.lower(), 0) + 1

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print()
for w in letters_count:
    if w.isalpha():
        print(f"The '{w}' character was found {letters_count[w]} times")
