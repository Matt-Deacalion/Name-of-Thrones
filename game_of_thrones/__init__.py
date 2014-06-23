import random
import string
from itertools import islice
from collections import defaultdict


class MarkovChain:
    """
    Entity which contains a chunk of text and a Markov chain generated from it.
    """
    sample_data = """
        tyrion lannister rock cersei baratheon stark ibben targaryen daena
        rhaenyra velaryon viserys aegon elaena naerys aemon daenerys martell
        blackfyre maekar aerion mararys valarr rhae daella syrio forel
        dothraki tywin sansa dontos yoren osha skagos hodor noye jeyne sandor
        clegane tyrell margaery eyrie davos tully arya snow artos mormont
        catelyn petry baelish melisandre ygritte jeor shae khal drogo saan
        salladhor cressen dagmer alton payne xaro illyrio qotho daario naharis
        prendahl gendry qyburn jaqen rorge armeca marillion beric dondarrion
        slynt ilyn hallyne mance orell tormund craster maester khalasar
    """

    def __init__(self, text=None, min_length=None, max_length=None):
        self.text = text if text else self.sample_data
        self.min_length = min_length if min_length else 4
        self.max_length = max_length if max_length else 10
        self.pairs = []

        for word in self.text.split():
            self.pairs += self.pair_symbols(self.sanitise_text(word))

        self.transition_tallies = self.get_transition_tallies()
        self.sum_transitions = self.get_sum_transitions()

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

    def get_transition_tallies(self, pairs=None):
        """
        Takes a list of tuples and returns a dict containing information about
        how often symbols appear after other symbols.
        """
        pairs = pairs if pairs else self.pairs
        tallies = defaultdict(lambda: defaultdict(int))

        # we remove the last pair because it doesn't transition anywhere
        pairs = pairs[:-1]

        for now, after in pairs:
            tallies[now][after] += 1

        return tallies

    def get_sum_transitions(self, tallies=None):
        """
        Takes a dict of dicts containing information about transition tallies
        and returns a dict of sum totals for each symbol.
        """
        tallies = tallies if tallies else self.transition_tallies
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
        letter = random.choice(list(self.transition_tallies.keys()))

        while True:
            yield letter
            letter = self.get_weighted_letter(letter)

    def word(self):
        """
        Generator that returns the next word indefinitely.
        """
        while True:
            length = random.randint(self.min_length, self.max_length)
            yield ''.join(islice(self.letter(), length))
