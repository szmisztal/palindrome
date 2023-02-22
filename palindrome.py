string = "potop"

def is_string_palindrome(string):
  return string == string[::-1]

answer = is_string_palindrome(string)
print(bool(answer))
