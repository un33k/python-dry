# -*- coding: utf-8 -*-

import unittest
from pydry.string import *

class TestDry(unittest.TestCase):

    def test_single_space(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_single_space(string)
        self.assertEquals(clean_string, "Hello\r\nWorld\t You Hoo")

    def test_single_line(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_single_line(string)
        self.assertEquals(clean_string, "Hello World       You  Hoo")

    def test_serialize(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = str_serialize_clean(string)
        self.assertEquals(clean_string, "Hello World You Hoo")

    def test_find_between_regex(self):
        string = "Hello\r\nWorld\t      You  Hoo Hoo <a href='foo' title='some title'>You Hoo</a>"
        start = "World\t"
        end = '<'
        # find substring the lazy way (shortest substring)
        substring = str_find_between_regex(start, end, string)
        self.assertEquals(substring, "      You  Hoo Hoo ")
        
        # find substring the greedy way (longest substring)
        substring = str_find_between_regex(start, end, string, lazy=False)
        self.assertEquals(substring, "      You  Hoo Hoo <a href='foo' title='some title'>You Hoo")

        start = "WORLD\t"
        # find substring the lazy way (shortest substring) -- CaseInsensitive
        substring = str_find_between_regex(start, end, string, case=False)
        self.assertEquals(substring, "      You  Hoo Hoo ")


    def test_find_between_regex_all(self):
        string = "Hello\r\nWorld\t      You  Hoo Hoo <a href='foo' title='some title'>You Hoo</a> Hello\r\nWorld\t      You  Hoo Hoo"
        start = "World\t"
        end = 'Hoo'
        # find substring the lazy way (shortest substring)
        substring = str_find_between_regex(start, end, string)
        self.assertEquals(substring.strip(), "You")

        # find substring the lazy way (shortest substring)
        substrings = str_find_between_regex(start, end, string, allmatch=True)
        self.assertEquals(len(substrings), 2)
        self.assertEquals(substrings[0].strip(), "You")
        self.assertEquals(substrings[1].strip(), "You")

    def test_find_between_search(self):
        string = "Hello\r\nWorld Hoo\t      You  You Hoo <a href='foo' title='some title'>You You</a>"
        start = "Hoo"
        end = '<'
        # find substring by searching from left to right. (matching the first "end")
        substring = str_find_between_search(start, end, string)
        self.assertEquals(substring, "\t      You  You Hoo ")
        
        # find substring by search from right to left. (matching the first "start")
        substring = str_find_between_search(start, end, string, reverse=True)
        self.assertEquals(substring, " <a href='foo' title='some title'>You You")

        start = "HOO"
        # find substring by searching from left to right. (matching the first "end") -- CaseInsensitive
        substring = str_find_between_search(start, end, string, case=False)
        self.assertEquals(substring, "\t      You  You Hoo ")


if __name__ == '__main__':
    unittest.main()


