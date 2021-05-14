import numpy
from mapper import *
from filter import *
from reducer import *
from train_matrx import *

from info import *

LANGUAGES = ['eng', 'nl']


def train_matrix(txt, lang):
    """
    Calls right functions to make and save a chance matrix
    
    @param  txt: list of combinations found in text
    @param lang: Language configuration
    """
    matrix = numpy.zeros((28, 28))
    for line in txt:
        m = reducer(line)
        matrix = numpy.add(matrix, m)
    
    chance_m = reducer_chance_matrix(matrix)

    numpy.save("trained_matrix/" + lang + "_trained", chance_m)

def train():
    """
    Train function. Uses outputs from a function as inputs to the next to produce two trained matrices.
    """

    for x in LANGUAGES:
        path = "train_" + x + "/train_data"
        lines_list = mapper_get_lines(path)
        updated_text = mapper_replace_punct(lines_list, leestekens)
        combi_list = filter_training(updated_text)

        train_matrix(combi_list, x)

#train()