import numpy
from mapper import *
from filter import *
from reducer import *
from train_matrx import *

from info import *



def train_matrix(txt):
    """
    """
    matrix = numpy.zeros((28, 28))
    for line in txt:
        m = reducer(line)
        matrix = numpy.add(matrix, m)
    
    chance_m = reducer_chance_matrix(matrix)

    numpy.save("eng_trained", chance_m)

def train():

    lines_list = mapper_get_lines()
    updated_text = mapper_replace_punct(lines_list, leestekens)
    combi_list = filter_training(updated_text)

    train_matrix(combi_list)
