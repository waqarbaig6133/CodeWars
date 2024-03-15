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
