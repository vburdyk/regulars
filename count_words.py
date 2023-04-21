import re

example = f"Hello, i`m Volodya. I`m 18, now i`m learning regular expressions and find solutions" \
          f" about how to find word in example. I try to write some identical word. For example this word can be word," \
          f"but idk\n"

print(example)
word = input("Above you can see example.\nChoose one word and write word which you want to find and change in the example: ")

matches = re.findall(r"\b" + re.escape(word) + r"\b", example)

count_words = len(matches)

for match in matches:
    new_example = re.sub(r"\b" + re.escape(match) + r"\b", match.upper(), example)

print("Word ", "'", word, "'", "in example using", count_words, "times")
print(new_example)
