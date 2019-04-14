def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    filtered = ''.join(filter(str.isalpha, sentence))
    setted = set(filtered.lower())
    if setted == set(alphabet):
        return True
    elif setted != set(alphabet):
        return False
