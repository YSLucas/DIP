from info import *

# Filter
def filter_training(txt):
    """
    Get all 2 letter combinations in text

    @param  txt: tekst waat combinaties uit gehaald worden
    @return    : lijst met combinaties in tekst
    """
    combinations = []
    for line in txt:
        for letter in range(0, len(line)):  
            try:
                res = line[letter] + line[letter + 1]
                # leesteken + spatie is niet relevant dus die combinaties kunnen eruit. "\n" zitten er ook tussen en die kunnen ook weg
                # en check of beide letters wel in het (aangepaste) alfabet zitten
                if (res[0] in abc and res[-1] in abc) and (res != "%_" and res != "_%" and "\n" not in res):
                    combinations.append([res])
            except:
                continue
    
    return combinations


def filter_validation(txt):
    """
    Get all 2 letter combinations in text.
    
    Different funtion was made to return in correct form
    
    @param  txt: tekst waat combinaties uit gehaald worden
    @return    : lijst met combinaties in tekst
    """
    combinations = []
    for line in txt:
        temp = []
        for letter in range(0, len(line)):  
            try:
                res = line[letter] + line[letter + 1]
                # leesteken + spatie is niet relevant dus die combinaties kunnen eruit. "\n" zitten er ook tussen en die kunnen ook weg
                # en check of beide letters wel in het (aangepaste) alfabet zitten
                if (res[0] in abc and res[-1] in abc) and (res != "%_" and res != "_%" and "\n" not in res):
                    temp.append(res)
            except:
                continue
        combinations.append(temp)
    
    return combinations
