import numpy as np

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        list_of_strings = self.matrix_string.split('\n')
        list_of_numbers = []
        for string in list_of_strings:
            strings_to_numbers = string.split(' ')
            list_of_numbers.append(tuple(int(number) for number in strings_to_numbers))
        self.matrix = np.array(list_of_numbers)


    def row(self, x):
        return self.matrix[x-1].tolist()

    def column(self, x):
        return self.matrix[0:, x-1].tolist()
