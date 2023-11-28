def palindrome(s):
    text = ''.join(char for char in s if char.isalpha() or char.isdigit())
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False

val = palindrome("0p")
print(val)