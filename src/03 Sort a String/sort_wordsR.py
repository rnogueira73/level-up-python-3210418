def sort_words(string):
    return " ".join(sorted(string.split(), key=len))

if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
