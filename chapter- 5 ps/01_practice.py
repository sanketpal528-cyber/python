words = {
    "paani": "water",
    "kese": "how"
}
word = input("enter a hindi word: ")
print("meaning:", words.get(word))
# .get function is used to get the value of a key in a dictionary. It returns None if the key is not present in the dictionary.