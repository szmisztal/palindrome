def palindrome():
    word = str(input("Word ?: "))
    rev = word[::-1]
    asd = rev == word
    print(bool(asd))

palindrome()