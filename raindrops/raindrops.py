def raindrops(number):
    sound = []
    factors_and_sounds = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    for factor in factors_and_sounds:
        if number % factor[0] == 0:
            sound.append(factor[1])
    return ''.join(sound) or str(number)
