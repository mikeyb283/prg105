with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def has_no_e(word):
    return word.find('e') == -1

total = len(word_list)
no_e = [word for word in word_list if has_no_e(word)]
percentage = float(len(no_e)) / total
print no_e
print '{:.2%}'.format(percentage) + " of the words do not have the letter e."
