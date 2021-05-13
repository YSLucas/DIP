from mapper import *
from filter import *
from reducer import *
from train_matrx import *
from info import *
import numpy


def main():
    """
    Main function
    """

    lines_list = mapper_get_lines()
    updated_text = mapper_replace_punct(lines_list, leestekens)
    combi_list = filter_validation(updated_text)

    nl, eng = numpy.load('trained_matrix/nl_trained.npy'), numpy.load('trained_matrix/eng_trained.npy')
    result = reducer_final(eng, nl, combi_list)
    print(f'In deze tekst zijn {result[0]} Nederlandse zinnen gevonden, en {result[1]} Engelse zinnen.')
    return result

main()