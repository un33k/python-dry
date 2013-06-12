import re

def string_clean(string):
    """ Clean text -- single space """
    txt = re.sub("\r\n|\n|\r|\t", ' ', string)
    txt = re.sub(" +", ' ', txt)
    return txt






