import pandas as pd
import numpy as np


# Method for generating a dictionary with probabilities of a certain character in one position from a word list
# Arguments: wordlist and the character number (first, second etc.)
def get_percentages_from_wordlist(wordlist, character):
    # Empty list of all letters in this position, count dictionary and total variable
    letters = []
    count = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    total = 0

    # Iterating through all words and extracting letters
    for word in wordlist:
        letters.append(word[character - 1:character])

    # Counting the letters and computing total
    for letter in letters:
        count[letter] += 1
    total = sum(count.values())

    # Converting total count to percenetage of total
    for letter in count:
        count[letter] /= total

    # Returning the count dictionary
    return count


# Function for computing the total percentage
# (e.g. sum of all percentages of the word's letters in their resp. positions
def get_percentage_for_word(word, pctlist):
    # Initializing zero variable
    pct = 0

    # Iterating through all the word's letters
    for i in range(5):
        pct += pctlist[i][word[i:i + 1]]

    # Returning the percentage number
    return pct

if __name__ == '__main__':

    # Read raw data from text file
    # You need a wordlist named "20k.txt" in the script directory for this.
    raw_data = pd.DataFrame(np.loadtxt('20k.txt', dtype=str))

    # Create empty list with five-letter words and fill it
    words = []

    # Append all words with length of five characters
    for word in raw_data[0]:
        if len(word) == 5 and word[4:5] != 's':
            words.append(word)
    print('Corpus size: '+str(len(words)))

    print(str(len(words))+" words in total.")

    # Creating empty percentages list
    percentages = []

    # Appending all the percentage dictionaries to percentages list for all words and all positions
    for i in range(5):
        percentages.append(get_percentages_from_wordlist(words, i + 1))
        list = percentages[i]
        list=sorted(list.items(), key=lambda x: x[1], reverse=True)
        print('Most likely letters for character #'+str(i+1))
        print(list)


    # Iterating through all words in the wordlist to get their percentage sums
    # and putting them in a list
    word_percentages = []
    for word in words:
        word_percentages.append(get_percentage_for_word(word, percentages))

    # Merging wordlist and percentages into a dictionary
    words_with_percentages = dict(zip(words, word_percentages))

    # Sorting the dictionary
    sorted = sorted(words_with_percentages.items(), key=lambda x: x[1], reverse=True)

    # Voilà!
    print('Words with the highest sum of probabilities for all letters:')
    print(sorted)
