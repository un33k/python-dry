# -*- coding: utf-8 -*-

import unittest
from pydry.string import string_clean

class TestDry(unittest.TestCase):

    def test_manager(self):
        string = "Hello\r\nWorld\t      You  Hoo"
        clean_string = string_clean(string)
        self.assertEquals(clean_string, "Hello World You Hoo")

if __name__ == '__main__':
    unittest.main()


