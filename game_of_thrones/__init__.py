import random
import string
from collections import defaultdict


class MarkovChain:
    """
    Entity which contains a chunk of text and a Markov chain generated from it.
    """
    def __init__(self, text):
        self.text = text

    def pair_symbols(self, text):
        """
        Takes an string and returns a list of tuples. For example:

            >>> pair_symbols('Arya')
            [('A', 'r'), ('r', 'y'), ('y', 'a')]
        """
        return [pair for pair in zip(text[0::1], text[1::1])]

    def sanitise_text(self, text):
        """
        Takes a string and returns a version of it that has no punctuation,
        no spaces and where all the letters are lower case.
        """
        return ''.join(
            [s for s in text.lower() if s in string.ascii_lowercase],
        )

    def get_transition_tallies(self, pairs):
        """
        Takes a list of tuples and returns a dict containing information about
        how often symbols appear after other symbols.
        """
        tallies = defaultdict(lambda: defaultdict(int))

        # we remove the last pair because it doesn't transition anywhere
        pairs = pairs[:-1]

        for now, after in pairs:
            tallies[now][after] += 1

        return tallies

    def get_sum_transitions(self, tallies):
        """
        Takes a dict of dicts containing information about transition tallies
        and returns a dict of sum totals for each symbol.
        """
        return {k: sum(v.values()) for k, v in tallies.items()}

    def get_weighted_letter(self, letter):
        """
        Takes a letter and returns a weighted random letter. With the weights
        being derived from our Markov Chain.
        """
        random_sum = random.randint(0, self.sum_transitions[letter] - 1)

        for after, weight in self.transition_tallies[letter].items():
            if random_sum < weight:
                return after

            random_sum -= weight

    def letter(self):
        """
        Generator that returns the next letter indefinitely.
        """
        letter = random.choice(self.transition_tallies.keys())

        while True:
            yield letter
            letter = self.get_weighted_letter(letter)
