from game_of_thrones import MarkovChain
import unittest

class MarkovChainTest(unittest.TestCase):

    def test_markovchain_class_exists(self):
        """
        Does the `MarkovChain` class exist?
        """
        self.assertTrue('MarkovChain' in globals())
