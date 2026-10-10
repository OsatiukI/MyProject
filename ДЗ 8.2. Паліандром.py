def is_palindrome(text):
    text_start = text.lower()
    text_clean = ""
    for char in text_start:
        if char.isalnum():
            text_clean += char
    text_return = text_clean[::-1]
    result = True
    if text_clean != text_return:
        result = False
    return result


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")