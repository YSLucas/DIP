import numpy
from numpy.matrixlib.defmatrix import matrix
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
            if line != "":
                res.append(line)
    
    return res

def mapper_replace_punct(text, sign):
    """
    Replace all punctuation with % and replace spaces with _

    @param  sign: leestekens
    @return     : text waar leestekens vervangen zijn
    """
    res = []
    for line in text:
        for i in sign:
            line = line.replace(i, "%")
        
        line = line.replace(" ", "_")
        line = line.lower()
        res.append(line)

    return res


# Filter
def filter_for_loop(txt):
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
                if res != "%_" and res != "_%" and "\n" not in res: 
                    combinations.append(res)

            except:
                pass
    
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
    updated_text = mapper_replace_punct(lines_list, leestekens)
    combi_list = filter_for_loop(updated_text)
    print(combi_list[0:100])
    # print(updated_text)


main()