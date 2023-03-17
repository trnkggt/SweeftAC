# Create a variable index that will hold
# the index of the greatest character in word.
# Iterate over the list of characters and
# find the first character, that will be
# greater than the index character, if it's
# found, swap the characters and return new word,
# else return nothing

def bigger_is_greater(T, word):
    index = None
    word_list = list(word)
    for i in range(len(word) - 1, -1, -1):
        if index is None:
            index = i
        else:
            if word_list[i] < word_list[index]:
                word_list[i], word_list[index] = word_list[index], word_list[i]
                word = ''.join(word_list)
                return word
            else:
                index = i
