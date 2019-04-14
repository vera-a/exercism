def is_armstrong(number):
    digits = []
    for d in str(number):
        digits.append(int(d) ** len(str(number)))
    sum_of_digits = sum(digits)
    if sum_of_digits == number:
        return True
    else:
        return False
