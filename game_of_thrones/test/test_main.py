from game_of_thrones import MarkovChain
from unittest import mock
import unittest


class MarkovChainTest(unittest.TestCase):

    def setUp(self):
        self.text = 'You know nothing Jon Snow!'

        self.transitions = [
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
        ]

        self.tallies = {
            'Y': {'o': 1},
            'o': {'u': 1, 't': 1, 'n': 1, 'w': 2},
            'u': {' ': 1},
            ' ': {'k': 1, 'n': 1, 'J': 1, 'S': 1},
            'k': {'n': 1},
            'n': {'o': 3, ' ': 1, 'g': 1},
            'w': {' ': 1, '!': 1},
            't': {'h': 1},
            'h': {'i': 1},
            'i': {'n': 1},
            'g': {' ': 1},
            'J': {'o': 1},
            'S': {'n': 1},
        }

        self.expected_transitions = {
            'Y': 1,
            ' ': 4,
            'o': 5,
            'u': 1,
            'k': 1,
            'n': 5,
            'w': 2,
            't': 1,
            'h': 1,
            'i': 1,
            'g': 1,
            'J': 1,
            'S': 1,
        }

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
            self.transitions,
        )

    def test_sanitise_text(self):
        """
        Does the `sanitise_text` method work correctly?
        """
        mc = MarkovChain(self.text)
        self.assertEqual(mc.sanitise_text(mc.text), 'youknownothingjonsnow')

    def test_get_transition_tallies(self):
        """
        Does the `get_transition_tallies` method work correctly?
        """
        mc = MarkovChain(self.text)

        for k, v in mc.get_transition_tallies(self.transitions).items():
            self.assertEqual(sum(v.values()), self.expected_transitions[k])

    def test_get_sum_transitions(self):
        """
        Does the `get_sum_transitions` method work correctly?
        """

        self.assertEqual(
            MarkovChain(self.text).get_sum_transitions(self.tallies),
            self.expected_transitions,
        )

    @mock.patch('game_of_thrones.random.randrange', autospec=True)
    def test_get_weighted_letter(self, mock_random_randrange):
        """
        Does the `get_weighted_letter` method work correctly?
        """
        mock_random_randrange.return_value = 0

        mc = MarkovChain(self.text)
        mc.transition_tallies = self.tallies
        mc.sum_transitions = self.expected_transitions

        self.assertEqual(mc.get_weighted_letter('Y'), 'o')
