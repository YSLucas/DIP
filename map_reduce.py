import numpy
from info import *


# Mappers
def mapper_get_lines():
    """
    
    """
    res = []
    with open("data/train_eng/Moby_Dick11.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            res.append(line)
    
    return res

def mapper_replace_punct(text, sign):
    """
    Replace all punctuation with % and replace spaces with _

    @param  sign: leestekens
    @return     : text waar leestekens vervangen zijn
    """
    with open("data/train_eng/Moby_Dick11.txt", "r", encoding="utf8") as f:
        txt = f.read()

        for i in sign:
            txt = txt.replace(i, "%")
        
        txt = txt.replace(" ", "_")
        txt = txt.lower()

    return txt


# Filter
def filter_for_loop(txt):
    """
    Get all 2 letter combinations in text

    @param  txt: tekst waat combinaties uit gehaald worden
    @return    : lijst met combinaties in tekst
    """
    combinations = []
    for letter in range(0, len(txt)):
        try:
            res = txt[letter] + txt[letter + 1]
            # leesteken + spatie is niet relevant dus die combinaties kunnen eruit. "\n" zitten er ook tussen en die kunnen ook weg
            if res != "%_" and res != "_%" and "\n" not in res: 
                combinations.append(res)

        except:
            print("Filtering done.")
    
    return combinations

# Reduce
def reducer():
    """
    """
    matrix = numpy.zeros((28, 28))

def main():
    """
    Main function
    """
    lines_list = mapper_get_lines()
    tt = mapper_for_loop(leestekens)
    ff = filter_for_loop(tt)
    # print(ff[5:100])


main()