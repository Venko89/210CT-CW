def remove_vowels():
    d = ["a","e","i","o","u"]
    word = "beautiful"
    for k in d:
        word = word.replace(k,"")
    print(word)
remove_vowels()
