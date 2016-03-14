import toolz.itertoolz as itertoolz
from markov.chain.markov_simple import markov_chain

class markov_text(markov_chain):

    def __init__(self, iterable, step_size=1):
        super(markov_text, self).__init__(iterable, step_size)

    def predict(self, n):
        """Returns a length of n chain. Returns a string instead of an array"""
        response = itertoolz.take(n, self)
        return " ".join(response)

    def search(self, term):
        """Searches through the nodes, and selects a start
        point that matches closest to the search term, also sets
        current state."""
        pass

    def respond(self, term, n):
        """Responsed to the given string, with a length of n terms"""
        self.search(self,term)
        return self.predict(self, n)

