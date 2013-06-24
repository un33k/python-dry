# -*- coding: utf-8 -*-

import datetime
import unittest
from pydry.generic import *

class TestGeneric(unittest.TestCase):

    def test_uuid(self):
        length = 31
        uu = get_uuid(length)
        self.assertEquals(len(uu), length)

        uu2 = get_uuid(length)
        self.assertNotEquals(uu, uu2)

    def test_to_binary_len(self):
        length = 20
        bin = get_to_binary(9, length)
        self.assertEquals(len(bin), length)

    def test_to_binary_value(self):
        length = 20
        one = '00000000000000000001'
        bin = get_to_binary(1, length)
        self.assertEquals(bin, one)

    def test_days_ago(self):
        days = 5
        five_days_ago = get_days_ago(days)
        this_day = five_days_ago + datetime.timedelta(days)
        today = datetime.date.today()
        self.assertEquals(this_day, today)

    def test_days_from_now(self):
        days = 5
        five_days_from_now = get_days_from_now(days)
        this_day = five_days_from_now - datetime.timedelta(days)
        today = datetime.date.today()
        self.assertEquals(this_day, today)








