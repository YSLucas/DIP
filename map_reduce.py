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
        # eerste letter resulteert altijd in \ufeff, dus die skip ik
        # Er raken geen combinaties veloren want hij begint zo alsnog bij de eerste letter
        for letter in range(1, len(line)):  
            try:
                res = line[letter] + line[letter + 1]
                # leesteken + spatie is niet relevant dus die combinaties kunnen eruit. "\n" zitten er ook tussen en die kunnen ook weg
                
                if (res[0] in abc or res[-1] in abc) and (res != "%_" and res != "_%" and "\n" not in res):
                    combinations.append([res])
            except:
                continue
    
    return combinations

# Reduce
def reducer(c):
    """
    """
    matrix = numpy.zeros((28, 28))
    for combination in c:
        left, right = combination[0], combination[-1]
        try:
            matrix[abc.index(left)][abc.index(right)] += 1
        except:
            continue
    
    return matrix

def train_matrix(txt):
    """
    """
    matrix = numpy.zeros((28, 28))
    for line in txt:
        m = reducer(line)
        matrix = numpy.add(matrix, m)
    print(matrix)

def main():
    """
    Main function
    """
    lines_list = mapper_get_lines()
    updated_text = mapper_replace_punct(lines_list, leestekens)
    combi_list = filter_for_loop(updated_text)

    trained_matrix = train_matrix(combi_list)
    result_matrix = reducer(combi_list)
    # print(result_matrix)

    # print(updated_text)


main()