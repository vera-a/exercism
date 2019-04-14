def distance(strand_a, strand_b):
    if len(a) != len(b):
        raise ValueError ('The Hamming distance is only defined for sequences of equal length')
    a = list(strand_a)
    b = list(strand_b)
    return sum(el_a != el_b for el_a, el_b in zip(a, b))
