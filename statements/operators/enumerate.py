
# enumerate == only iterables!, returns index and property
index_count = 0
for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count, letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item) # return tuple

# with tuple unpacking
word = 'abcde'
for index, item in enumerate(word):
    print(index)
    print(letter)
    print('\n')