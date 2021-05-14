import numpy
from mapper import *
from filter import *
from reducer import *
from train_matrx import *

from info import *

LANGUAGES = ['eng', 'nl']


def train_matrix(txt, lang):
    """
    """
    matrix = numpy.zeros((28, 28))
    for line in txt:
        m = reducer(line)
        matrix = numpy.add(matrix, m)
    
    chance_m = reducer_chance_matrix(matrix)

    numpy.save("trained_matrix/" + lang + "_trained", chance_m)

def train():

    for x in LANGUAGES:
        path = "train_" + x + "/train_data"
        lines_list = mapper_get_lines(path)
        updated_text = mapper_replace_punct(lines_list, leestekens)
        combi_list = filter_training(updated_text)

        train_matrix(combi_list, x)
