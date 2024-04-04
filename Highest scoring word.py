'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
import string
def high(x):
    alphabets = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    letters = list(x)
    individual_score = []
    word_score = []
    z = []
    a = len(letters)
    i = 1
    for n in letters:
        if n == ' ':
            total_word = sum(individual_score)
            word_score.append(total_word)
            individual_score.clear()
            i+=1
        elif i == a:
            score = alphabets.index(n) + 1
            individual_score.append(score)
            total_word = sum(individual_score)
            word_score.append(total_word)
            
            i+=1
        else:
            score = alphabets.index(n) + 1
            individual_score.append(score)
            i+=1
    words = x.split()
    max_score = max(word_score)
    max_placement = word_score.index(max_score)
    return(words[max_placement])
