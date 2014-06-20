class MarkovChain:
    """
    Entity which contains a chunk of text and a Markov chain generated from it.
    """
    def __init__(self, text):
        self.text = text

    def pair_symbols(self, text):
        return [pair for pair in zip(text[0::1], text[1::1])]
