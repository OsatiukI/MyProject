def popular_words (text, words):
    text_red = text.lower().split()
    text_list = {}
    for word in words:
        text_list[word] = text_red.count(word)
    return text_list



assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
