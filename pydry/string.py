import re

def str_single_space(string):
    """ Converts one or more spaces into a single space """
    txt = re.sub(" +", ' ', string)
    return txt

def str_single_line(string):
    """ Converts a content with multiple line into a single line content """
    txt = re.sub("\r\n|\n|\r|\t", ' ', string)
    return txt

def str_serialize_clean(string):
    """ Converts content into a single line with single spaces """
    txt = str_single_space(str_single_line(string))
    return txt

def str_find_between_regex(start, end, string, lazy=True, options=re.DOTALL|re.MULTILINE, all=False):
    """ Returns substring btween two strings tags. all=(returns all matches), lazy=(return shortest match)"""
    pattern = '(?<={}){}(?={})'.format(re.escape(start), '(.*?)' if lazy else '(.*)', re.escape(end))
    match = re.findall(pattern, string, options)
    if match:
        if all:
            return match
        else:
            return match[0]
    return ''

def str_find_between_search(start, end, string, reverse=False):
    try:
        if reverse:
            start = string.rindex(start) + len(start)
            end = string.rindex(end, start)
        else:
            start = string.index(start) + len(start)
            end = string.index(end, start)
        return string[start:end]
    except ValueError:
        return ""






