from info import *
import numpy

# Reduce
def reducer(c):
    """
    """
    matrix = numpy.zeros((28, 28))
    for combination in c:
        left, right = combination[0], combination[-1]
        try:
            matrix[abc.index(left)][abc.index(right)] += 1 # find right place in matrix and add 1
        except:
            # double check: if one of the letters isnt in the alphabet skip this one and continue
            continue 
    
    return matrix


def reducer_chance_matrix(m):
    """
    Convert a frequence matrix to a chance matrix
    """
    total = numpy.sum(m) # total letter combinations analysed
    
    with numpy.nditer(m, op_flags=['readwrite']) as it:
        for x in it:
            if x != 0:
                x[...] = round(x / total * 100, 4) # chance x to its chance that it occurs
            
    return m
    



def reducer_final(eng_m, nl_m, c):
    """
    
    @param eng_m: english trained matrix numpy array
    @param nl_m: dutch trained matrix numpy array
    @param c: list van combinaties die voorkomen per zin
    """
    nl_count = 0    # hough bij hoeveel nederlandse zinnen er zijn gevonden
    eng_count = 0   # houdt bij hoveel engelse zinnen er zijn gevonden
    for line in c:  # loopt door de tekst heen per line
        # De matrices zijn gevuld met kansen. Per combinatie die in een zin voorkomt
        # pakt het algoritme de bijbehorende kans en telt die bij de totale kans dat een
        # zin nederlands of engels is op. De taal met het hoogste getal aan het einde 
        # wordt als waarheid genomen.
        eng = 0   
        nl = 0
        for combination in line:
            left, right = abc.index(combination[0]), abc.index(combination[-1]) # vind juiste index voor matrices
            oem = eng_m[left][right]    # On English Matrix. De kans dat de combinatie voorkomt in het engels
            odm = nl_m[left][right]     # On Dutch Matrix. De kans dat de combinatie voorkomt in het engels
            eng += oem  # tel de kans op bij het totaal (voor sepcifieke zin)
            nl += odm
        
        # er is nu een complete zin gecheckt -> kijk welk getal groter is en tel één bij de telling op
        # Een gelijkspel zal zeer waarschijnlijk niet voorkomen omdat de kansen op 3 decimalen zijn afgerond
        if eng > nl:
            eng_count += 1
        else:
            nl_count += 1
        
        #reset waardes voor zin en ga door naar de volgende zin
        eng, nl = 0, 0  
    
    return nl_count, eng_count
