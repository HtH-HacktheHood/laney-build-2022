from unicodedata import name
import unittest
from hero import *

class TestHero(unittest.TestCase):

    def test_init(self):
        # first check if hero.name is a string and if hero.starting_health is integer
        self.assertEqual(type(Hero().name),type(""))
        self.assertEqual(type(Hero().starting_health),type(0))
        self.assertRaises(AssertionError, Hero(), name)