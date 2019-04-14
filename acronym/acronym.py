import re

def abbreviate(words):
    acronym = re.findall(r"(\w)(?:\w*\'?s?)", words)
    return ''.join(acronym).upper()

