import string


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
