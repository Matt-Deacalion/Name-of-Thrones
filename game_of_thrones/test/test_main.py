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

    def test_pair_symbols(self):
        """
        Does the `pair_symbols` method work correctly?
        """
        self.assertEqual(
            MarkovChain(self.text).pair_symbols(self.text),
            [
                ('Y', 'o'),
                ('o', 'u'),
                ('u', ' '),
                (' ', 'k'),
                ('k', 'n'),
                ('n', 'o'),
                ('o', 'w'),
                ('w', ' '),
                (' ', 'n'),
                ('n', 'o'),
                ('o', 't'),
                ('t', 'h'),
                ('h', 'i'),
                ('i', 'n'),
                ('n', 'g'),
                ('g', ' '),
                (' ', 'J'),
                ('J', 'o'),
                ('o', 'n'),
                ('n', ' '),
                (' ', 'S'),
                ('S', 'n'),
                ('n', 'o'),
                ('o', 'w'),
                ('w', '!'),
            ],
        )
