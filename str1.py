word = input("Enter you name: ")
words = word.split()
capitalized_words = word.capitalize()
reversed_words = capitalized_words[::-1]
print(words)
result = " ".join(reversed_words)
print(result)



