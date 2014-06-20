from game_of_thrones import MarkovChain
import unittest

class MarkovChainTest(unittest.TestCase):

    def setUp(self):
        self.text = 'You know nothing Jon Snow!'

    def test_markovchain_class_exists(self):
        """
        Does the `MarkovChain` class exist?
        """
        self.assertTrue('MarkovChain' in globals())

    def test_text_initialised(self):
        """
        Does the text attribute get assigned correctly?
        """
        self.assertEqual(self.text, MarkovChain(self.text).text)
