# Iterate over each word in words list.
# If word is already in dict its value is
# incremented by one, if it is not it is created
# with value zero.

def count_occur(n, words):
    if n == 1:
        return 1, [1]

    temp = {}
    for i in words:
        temp[i] = temp.get(i, 0) + 1

    return len(temp), list(temp.values())


print(count_occur(12010, ['abc', 'def', 'ghi', 'abc', 'jkl', 'def', 'pqr', 'stu', 'def', 'vwx'] + ['xyz']*1000 +
                  ['abc']*1000+['gbe']*10000))