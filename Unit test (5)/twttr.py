#removes vowels and makes all lowercase


def main():
    word = input("word to be shortened: ")
    s_word = shorten(word)
    print(s_word)

def shorten(word):
    word = word.lower()
    for char in word:
        word = word.replace("a", "")
        word = word.replace("e", "")
        word = word.replace("i", "")
        word = word.replace("o", "")
        word = word.replace("u", "")
    return word


if __name__ == "__main__":
    main()