import unittest
from True2chisla import Dvachisla
class TEST_True2chisla(unittest.TestCase):

    def setUp(self):
        self.dvachisla = Dvachisla

    def testdvachisla(self):
        self.dvachisla = Dvachisla
        action = Dvachisla()
        actiontoassert = action.inputOfTwo([1, 2, 3, 4, 5], [1, 2, 9, 7])
        self.assertTrue(actiontoassert==1)

# self.assertTrue('FOO'.isupper())