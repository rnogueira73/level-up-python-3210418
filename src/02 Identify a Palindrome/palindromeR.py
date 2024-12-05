def is_palindrome(string):
    string = "".join(c for c in string if c.isalpha()).lower()
    list_of_word = list(string)
    stringR = ""
    for i in range(1,len(string) + 1):
        stringR = stringR + list_of_word.pop()
    return (stringR == string)

def is_palindrome_v2(string):
    string = "".join(c for c in string if c.isalpha()).lower()
    backwards = string[::-1]
    return (backwards == string)

if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome('level'))
    print(is_palindrome_v2("Go hang a salami, I'm a lasagna hog."))  # true
