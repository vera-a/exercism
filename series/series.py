def slices(series, length):
    list_of_slices = []
    i = 0
    if 1 <= length <= 5 and len(series) > 0:        
        for element in series:
            list_of_slices.append(series[0+i:length+i])
            i += 1
            if i > length:
                break
            elif length == len(series):
                break
    else:
        raise ValueError('The length or the slice is out of range')
    return list_of_slices
