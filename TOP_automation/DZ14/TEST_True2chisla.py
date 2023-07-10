import unittest
from True2chisla import Dvachisla
class TEST_True2chisla(unittest.TestCase):

    def setUp(self):
        self.dvachisla = Dvachisla

    def testdvachisla(self):
        self.assertTrue(self.dvachisla.inputOfTwo([1, 2, 3, 4, 5], [1, 2, 9, 7])==1)

# self.assertTrue('FOO'.isupper())