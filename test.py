# a = []
# n = int(input("n="))
# for i in range(1 ,n):
#     if n % i == 0:
#         a.append(i)
# print(a)
def generate_words(letters, n_count, word_length):
    if word_length == 0:
        if n_count >= 2:
            return ['']
        else:
            return []
    words = []
    for letter in letters:
        if letter == 'N':
            new_n_count = n_count + 1
        else:
            new_n_count = n_count
        subwords = generate_words(letters, new_n_count, word_length - 1)
        for subword in subwords:
            words.append(letter + subword)
    return words

letters = ['A', 'D', 'H', 'V', 'N', 'N']
words = generate_words(letters, 0, 6)
print(len(words))