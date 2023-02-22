string = "kajak"

def is_string_palindrome(string):
  return string == string[::-1]

print(bool(is_string_palindrome))