from functools import reduce

def verify(isbn):
    if len(isbn) > 0 and isbn[-1] == 'X':
        isbn = isbn.replace('X', '10')
    list_of_digits = [int(element) for element in isbn if element.isdigit()]
    if isbn[-2:] == '10':
        list_of_digits[-2] = 10
        list_of_digits.pop(-1)
    i = 0
    verified_list = []
    if len(list_of_digits) !=  10:
        return False
    for n in range(10, 0, -1):
        verified_list.append(list_of_digits[i] * n)
        i += 1
    result = reduce(lambda x, y: x + y, verified_list)
    return result % 11 == 0     
