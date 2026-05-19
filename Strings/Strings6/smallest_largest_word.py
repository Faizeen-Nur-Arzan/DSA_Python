def smallest_largest_words(sentence):
    sentence += " "
    word = ""
    list_of_words = []
    for i in sentence:
        if not i == " ":
            word += i
        else:
            list_of_words.append(word)
            word = ""
    
    largest = list_of_words[0]
    smallest = list_of_words[0]
    for j in list_of_words:
        if len(j) > len(largest):
            largest = j
        elif len(j) < len(smallest):
            smallest = j
        else:
            continue
    
    return largest, smallest

print(smallest_largest_words("Chenge re tenge bengieds"))