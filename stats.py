
def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_letter_count(text):
    letters = {}
    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def sort_letter_count(letters):
    list_of_dict = []
    for i in letters:
        data = {"char": i, "num": letters[i]}
        list_of_dict.append(data)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict