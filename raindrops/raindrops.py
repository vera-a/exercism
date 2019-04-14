def raindrops(number):
    result = ''
    if int(number) % 3 == 0:
        result += 'Pling'
    if int(number) % 5 == 0:
        result += 'Plang'
    if int(number) % 7 == 0:
        result += 'Plong'
    return result or str(number)
