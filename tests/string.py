# -*- coding: utf-8 -*-

import unittest
from pydry.string import *

class TestStringRegEx(unittest.TestCase):

    def test_find_between_regex(self):
        string = "Hello\r\nWorld\t      You  Hoo Hoo <a href='foo' title='some title'>You Hoo</a>"
        start = "World\t"
        end = '<'
        # find substring the lazy way (shortest substring)
        substring = str_find_between_regex(string, start, end)
        self.assertEqual(substring, "      You  Hoo Hoo ")
        
        # find substring the greedy way (longest substring)
        substring = str_find_between_regex(string, start, end, lazy=False)
        self.assertEqual(substring, "      You  Hoo Hoo <a href='foo' title='some title'>You Hoo")

        start = "WORLD\t"
        # find substring the lazy way (shortest substring) -- CaseInsensitive
        substring = str_find_between_regex(string, start, end, case=False)
        self.assertEqual(substring, "      You  Hoo Hoo ")

        start = ""
        # find substring the lazy way (shortest substring from the start of string)
        substring = str_find_between_regex(string, start, end)
        self.assertEqual(substring, "Hello\r\nWorld\t      You  Hoo Hoo ")

        start = "World\t"
        end = ""
        # find substring the lazy way (shortest substring from the start to end of string)
        substring = str_find_between_regex(string, start, end)
        self.assertEqual(substring, "      You  Hoo Hoo <a href='foo' title='some title'>You Hoo</a>")

    def test_find_between_regex_all(self):
        string = "Hello\r\nWorld\t      You  Hoo Hoo <a href='foo' title='some title'>You Hoo</a> Hello\r\nWorld\t      You  Hoo Hoo"
        start = "World\t"
        end = 'Hoo'
        # find substring the lazy way (shortest substring)
        substring = str_find_between_regex(string, start, end)
        self.assertEqual(substring.strip(), "You")

        # find substring the lazy way (shortest substring)
        substrings = str_find_between_regex(string, start, end, allmatch=True)
        self.assertEqual(len(substrings), 2)
        self.assertEqual(substrings[0].strip(), "You")
        self.assertEqual(substrings[1].strip(), "You")

class TestString(unittest.TestCase):

    def test_single_space(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_single_space(string)
        self.assertEqual(clean_string, "Hello\r\nWorld\t You Hoo")

    def test_single_dash(self):
        string = "Hello\r\nWorld\t      --You  Hoo-------"
        clean_string = str_single_dash(string)
        self.assertEqual(clean_string, "Hello\r\nWorld\t      -You  Hoo-")

    def test_single_line(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_single_line(string)
        self.assertEqual(clean_string, "Hello World       You  Hoo")

    def test_serialize(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_serialize_clean(string)
        self.assertEqual(clean_string, "Hello World You Hoo")

    def test_find_between_search(self):
        string = "Hello\r\nWorld Hoo\t      You  You Hoo <a href='foo' title='some title'>You You</a>"
        start = "Hoo"
        end = '<'

        # find substring by searching from left to right.
        substring = str_find_between_tags(string, start, end)
        self.assertEqual(substring, "\t      You  You Hoo ")

        # find substring by searching from left to right. (case=False)
        start = "HOO"
        substring = str_find_between_tags(string, start, end, case=False)
        self.assertEqual(substring, "\t      You  You Hoo ")

        # find substring by searching from right to left.
        start = "Hoo"
        substring = str_find_between_tags_r(string, start, end)
        self.assertEqual(substring, " <a href='foo' title='some title'>You You")

        # find substring by searching from right to left. (case=False)
        start = "HOO"
        substring = str_find_between_tags_r(string, start, end, case=False)
        self.assertEqual(substring, " <a href='foo' title='some title'>You You")

        # find substring by searching from left to right. (start of string to end tag)
        start = ''
        substring = str_find_between_tags(string, start, end)
        self.assertEqual(substring, "Hello\r\nWorld Hoo\t      You  You Hoo ")

        # find substring by searching from right to left. (start tag to end of string)
        start = "Hoo"
        end = ''
        substring = str_find_between_tags_r(string, start, end)
        self.assertEqual(substring, " <a href='foo' title='some title'>You You</a>")

        # find substring by searching from right to left. (start tag to end of string) (case=False)
        start = "HOO"
        end = ''
        substring = str_find_between_tags_r(string, start, end, case=False)
        self.assertEqual(substring, " <a href='foo' title='some title'>You You</a>")


    def test_find_all_between_search(self):
        string = "A\tAYou  You HooB\nB\nWorld Hoo\t A\tAYou  You HooB\nB <a href='foo' title='some title'>A\tAYou  You HooB\nB</a>"
        start = "A\tA"
        end = 'B\nB'

        # find all substring by searching from left to right.
        substrings = str_find_all_between_tags(string, start, end)
        self.assertEqual(len(substrings), 3)

        # find all substring by searching from left to right. case=False
        start = "A\ta"
        substrings = str_find_all_between_tags(string, start, end, case=False)
        self.assertEqual(len(substrings), 3)

        # find substring the lazy way (shortest substring) regex
        start = "A\tA"
        substrings = str_find_between_regex(string, start, end, allmatch=True)
        self.assertEqual(len(substrings), 3)

        # find substring the lazy way (shortest substring) regex (case=False)
        start = "A\ta"
        substrings = str_find_between_regex(string, start, end, allmatch=True, case=False)
        self.assertEqual(len(substrings), 3)

class TestStringTokenizerCase(unittest.TestCase):
    """ Tokenizer Test """

    def test_tokenizer_test(self):
        text = "I am a test -You -are -NOT -a -test"
        includes, excludes = str_text_tokenizer(text)
        self.assertEqual(' '.join(includes), "I am a test")
        self.assertEqual(' '.join(excludes), "You are NOT a test")


class TestStringUniDecode(unittest.TestCase):
    """ Decode a unicode string """

    def test_unidecode(self):
        txt = '影師嗎'
        r = str_unicode_translate(txt)
        self.assertEqual(r, "Ying Shi Ma ")

class TestStringTruncate(unittest.TestCase):
    """ Truncate String """

    def test_truncate(self):

        txt = "This is test number one"
        # no truncation
        r = str_smart_truncate(txt)
        self.assertEqual(r, txt)

        # truncate 5
        r = str_smart_truncate(txt, 5)
        self.assertEqual(r, "This")

        # truncate max larger than str len
        r = str_smart_truncate(txt, 51)
        self.assertEqual(r, txt)

        # truncate respecting world boundary
        r = str_smart_truncate(txt, 9, word_boundaries=True)
        self.assertEqual(r, "This is")

        # truncate respecting world boundary with dash separator
        txt = "This-is-test-number-one"
        r = str_smart_truncate(txt, 9, word_boundaries=True, separator='-')
        self.assertEqual(r, "This-is")

        # truncate respecting world boundary with dash separator single word
        txt = "This-"
        r = str_smart_truncate(txt, 9, word_boundaries=True, separator='-')
        self.assertEqual(r, "This")

        # truncate respecting world boundary with dash separator single word max less than word len
        txt = "ThisIsALongWord-"
        r = str_smart_truncate(txt, 9, word_boundaries=True, separator='-')
        self.assertEqual(r, "ThisIsALo")

        # truncate respecting world boundary with dash separator single word max bigger than word len
        txt = "ThisIsALongWord-"
        r = str_smart_truncate(txt, 19, word_boundaries=True, separator='-')
        self.assertEqual(r, "ThisIsALongWord")





