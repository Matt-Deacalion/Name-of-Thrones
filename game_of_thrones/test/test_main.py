from game_of_thrones import MarkovChain
from itertools import islice
import unittest
import string

# Python 3
try:
    from unittest import mock
except ImportError:
    import mock


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
            'w': {' ': 1},
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
            'w': 1,
            't': 1,
            'h': 1,
            'i': 1,
            'g': 1,
            'J': 1,
            'S': 1,
        }

    def test_markovchain_class_exists(self):
        self.assertTrue('MarkovChain' in globals())

    def test_text_initialised(self):
        self.assertEqual(self.text, MarkovChain(self.text).text)

    def test_pair_symbols(self):
        self.assertEqual(
            MarkovChain(self.text).pair_symbols(self.text),
            self.transitions,
        )

    def test_sanitise_text(self):
        mc = MarkovChain(self.text)
        self.assertEqual(mc.sanitise_text(mc.text), 'youknownothingjonsnow')

    def test_get_transition_tallies(self):
        mc = MarkovChain(self.text)

        for k, v in mc.get_transition_tallies(self.transitions).items():
            self.assertEqual(sum(v.values()), self.expected_transitions[k])

    def test_get_sum_transitions(self):
        self.assertEqual(
            MarkovChain(self.text).get_sum_transitions(self.tallies),
            self.expected_transitions,
        )

    @mock.patch('game_of_thrones.random.randint', autospec=True)
    def test_get_weighted_letter(self, mock_random_randint):
        mock_random_randint.return_value = 0

        mc = MarkovChain(self.text)
        mc.transition_tallies = self.tallies
        mc.sum_transitions = self.expected_transitions

        self.assertEqual(mc.get_weighted_letter('Y'), 'o')
        self.assertTrue(mc.get_weighted_letter('o') in 'utnw')

    @mock.patch('game_of_thrones.random.choice', autospec=True)
    def test_letter(self, mock_random_randchoice):
        mock_random_randchoice.return_value = 'Y'

        mc = MarkovChain(self.text)
        mc.transition_tallies = self.tallies
        mc.sum_transitions = self.expected_transitions

        word = ''.join(islice(mc.letter(), 3))

        self.assertEqual(word[0], 'Y')
        self.assertEqual(word[1], 'o')
        self.assertTrue(word[2] in 'utnw')

    def test_word(self):
        expected_letters = list(self.expected_transitions.keys())

        try:
            unexpected_letters = string.ascii_letters.translate(
                {ord(i): None for i in expected_letters},
            )
        except TypeError:
            unexpected_letters = string.ascii_letters.translate(
                None,
                ''.join(expected_letters),
            )

        mc = MarkovChain(self.text, min_length=5, max_length=5)
        mc.transition_tallies = self.tallies
        mc.sum_transitions = self.expected_transitions

        words = ''.join(islice(mc.word(), 3))

        for word in words:
            self.assertTrue(len(word), 5)

            for letter in word:
                self.assertTrue(letter in expected_letters)
                self.assertFalse(letter in unexpected_letters)

    def test_pairwise_no_spaces(self):
        """
        Make sure there are no transitions between words.
        """
        mc = MarkovChain('One two')
        self.assertFalse(('e', 't') in mc.pairs)

    @mock.patch.object(MarkovChain, 'word', autospec=True)
    def test_unique_word(self, mock_markovchain):
        mc = MarkovChain(self.text)
        mock_markovchain.return_value = ['One', 'Two', 'Three', 'One']

        self.assertEqual(
            [word for word in mc.unique_word()],
            ['One', 'Two', 'Three'],
        )

    @mock.patch.object(MarkovChain, 'get_weighted_letter', autospec=True)
    @mock.patch('game_of_thrones.random.choice', autospec=True)
    @mock.patch('game_of_thrones.random.randint', autospec=True)
    def test_consecutive_bugfix(
        self,
        mock_rand_int,
        mock_rand_choice,
        mock_get_weighted_letter,
    ):
        """
        Regression test for bug #1. There should never be 3 or more
        consecutive characters in a generated word.
        """
        generated = 'Scooooooooby!'
        expected_output = 'Scooby!'

        mc = MarkovChain(self.text)

        mock_rand_int.return_value = len(expected_output)
        mock_rand_choice.return_value = generated[0]
        mock_get_weighted_letter.side_effect = iter(generated[1:])

        self.assertEqual(next(mc.word()), expected_output)
