def get_word_frequencies(words):
    data = dict()
    for word in words:
        if word in data:
            data[word] += 1
        else:
            data.update({word: 1})
    return data
