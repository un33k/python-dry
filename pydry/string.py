# -*- coding: utf-8 -*-

import re
import sys
import types
import unicodedata
from unidecode import unidecode

try:
    from htmlentitydefs import name2codepoint
except ImportError:
    from html.entities import name2codepoint

single_line_pattern = re.compile("\r\n|\n|\r|\t")
single_space_pattern = re.compile(' +')
single_dash_pattern = re.compile('-+')
char_entry_pattern = re.compile('&(%s);' % '|'.join(name2codepoint))

# split on double-quotes, single-quotes, and continuous non-whitespace characters.
line_split_pattern = re.compile('("[^"]+"|\'[^\']+\'|\S+)')

def str_single_space(string):
    """ Converts more than one consecutive spaces into a single space """

    txt = single_space_pattern.sub(' ', string)
    return txt

def str_single_dash(string):
    """ Converts more than one consecutive dash into a single space """

    txt = single_dash_pattern.sub('-', string)
    return txt

def str_single_line(string):
    """ Converts a content with multiple line into a single line content """

    txt = single_line_pattern.sub(' ', string)
    return txt

def str_serialize_clean(string):
    """ Converts content into a single line with single spaces """

    txt = str_single_space(str_single_line(string))
    return txt

def str_unicode(string):
    """ Convers text to unicode """

    if type(string) != types.UnicodeType:
        string = unicode(string, 'utf-8', 'ignore')
    return string

def str_unicode_translate(string):
    """ decode unicode ( 影師嗎 = Ying Shi Ma) """

    text = unidecode(str_unicode(string))
    return str_unicode(text)

def str_smart_truncate(string, max_length=0, word_boundaries=False, separator=' '):
    """ Truncate a string """

    string = string.strip(separator)

    if not max_length:
        return string

    if len(string) < max_length:
        return string

    if not word_boundaries:
        return string[:max_length].strip(separator)

    if separator not in string:
        return string[:max_length]

    truncated = ''
    for word in string.split(separator):
        if word:
            next_len = len(truncated) + len(word) + len(separator)
            if next_len <= max_length:
                truncated += '{0}{1}'.format(word, separator)
    if not truncated:
        truncated = string[:max_length]
    return truncated.strip(separator)


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
    """ Returns a substring between two string tags """

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

def str_find_all_between_tags(string, start='', end='', case=True):
    """ Returns all substrings between two string tags """

    if not case:
        string_orig = string
        string = string.lower()
        start = start.lower()
        end = end.lower()

    results = []
    while True:

        if start:
            s = string.find(start)
        else:
            s = 0

        if end:
            e = string.find(end, s+len(start))
        else:
            e = len(string)

        if s < 0 or e < 0:
            break

        if not case:
            match = string_orig[s+len(start):e]
            string_orig = string_orig[e+len(end):]
        else:
            match = string[s+len(start):e]
        results.append(match)
        string = string[e+len(end):]
    return results


def str_find_between_tags_r(string, start='', end='', case=True):
    """ Returns a substring between two string tags - Start from end of string """

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

def str_text_tokenizer(string):
    """ 
    Tokenize the input string and return two lists, exclude list is for words that
    start with a dash (ex: -word) and include list is for all other words
    """

    # Return the list of keywords.
    keywords = [ single_dash_pattern.sub('-', single_space_pattern.sub(' ', t.strip(' "\''))) \
                for t in line_split_pattern.findall(string) if len(t.strip(' "\'')) > 0 ]
    include = [ word for word in keywords if not word.startswith('-') ]
    exclude = [ word.lstrip('-') for word in keywords if word.startswith('-') ]
    return include, exclude







