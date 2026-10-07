def second_index(text, some_str):
    start_letter = text.find(some_str)
    next_letter = text.find(some_str, start_letter +1)
    if next_letter == -1:
        return None
    return next_letter


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')