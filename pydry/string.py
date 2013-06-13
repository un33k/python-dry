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

def str_find_between_regex(string, start='', end='',  lazy=True, options=re.DOTALL|re.MULTILINE, allmatch=False, case=True):
    """ Returns substring between two strings tags. all=(returns all matches), lazy=(return shortest match)"""

    if not case:
        options |= re.IGNORECASE

    pattern = '{0}{1}{2}'.format('(?<={0})'.format(re.escape(start)) if start else '^',
                                 '(.*?)' if lazy else '(.*)',
                                 '(?={0})'.format(re.escape(end)) if end else '$')
    match = re.findall(pattern, string, options)
    if match:
        if allmatch:
            return match
        else:
            return match[0]
    return ''

def str_find_between_tags(string, start='', end='', case=True):
    """ Returns substring between two strings tags """

    if not case:
        string_orig = string
        string = string.lower()
        start = start.lower()
        end = end.lower()

    if start:
        s = string.find(start)
    else:
        s = 0

    if end:
        e = string.find(end, s+len(start))
    else:
        e = len(string)

    if s < 0 or e < 0:
        return ''

    if not case:
        return string_orig[s+len(start):e]
    return string[s+len(start):e]
    

def str_find_between_tags_r(string, start='', end='', case=True):
    """ Returns substring between two strings tags - Start from end of string """

    if not case:
        string_orig = string
        string = string.lower()
        start = start.lower()
        end = end.lower()

    if end:
        e = string.rfind(end)
    else:
        e = len(string)

    if start:
        if end:
            s = string.rfind(start, len(end))
        else:
            s = string.rfind(start)
    else:
        s = 0

    if s < 0 or e < 0:
        return ''

    if not case:
        return string_orig[s+len(start):e]
    return string[s+len(start):e]






