import numpy


leestekens = [".", ",", ":", ";", "\'", "\"", "-", "_", "!", "?", "(", ")"]

# Mapper
def mapper_for_loop(sign):
    """
    Replace all punctuation with % and replace spaces with _

    @param  sign: leestekens
    @return     : text waar leestekens vervangen zijn
    """
    with open("data/Moby_Dick.txt", "r", encoding="utf8") as f:
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
    pass

def main():
    """
    Main function
    """
    tt = mapper_for_loop(leestekens)
    ff = filter_for_loop(tt)
    print(ff[5:100])


main()