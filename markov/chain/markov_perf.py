import random as r
import toolz
from markov.probability.probabilities import get_probabilites
from markov.probability.windows import get_windows
import jsonpickle


class markov_perf:
    """Performant Markov change to be used with large datasets"""

    def __init__(self, iterable, step_size=1):
        self.step_size = step_size
        windows = get_windows(iter(iterable), step_size)
        self.chain = get_probabilites(windows)
        self.current_state = r.choice(list(self.chain.keys()))

    def __init__(self, step_size, current_state, chain):
        self.step_size = step_size
        self.current_state = current_state
        self.chain = chain

    def __str__(self):
        """Display Chain Structure"""
        string = ""
        for key, val in self.chain.items():
            string += "{key:-<40}{val:->40} \n".format(
                key=str(key), val=str(val))
        return string

    def __len__(self):
        """Returns the total number of links in the chain"""
        return len(self.chain)

    def __getitem__(self, key):
        """Gets the next prediction given the input key"""
        if len(key) != self.step_size or not isinstance(key, tuple):
            raise TypeError(
                "Type must be of the same length as step_size and must be a tuple")
        if key not in self.chain.keys():
            raise KeyError("Item is not found in this chain")
        options = self.chain[key]
        choice = r.random()
        for opt in options:
            if opt[1] > choice:
                return opt[0]
            else:
                choice = choice - opt[1]

    def __iter__(self):
        """Iterates over the chain yeilding values based on seed"""
        return self

    def __next__(self):
        try:
            next_item = self[self.current_state]
        except KeyError:
            raise StopIteration
        new_state = list(self.current_state[1:])
        new_state.append(next_item)
        self.current_state = tuple(new_state)
        return next_item

    def __contains__(self, item):
        """"Returns true if item is a link in the chain"""
        return item in self.chain.keys()

    def set_state(self, state):
        """Defines the seed to be used while iterating over the chain. Seed only determines the start value,
        not the subsequent values."""
        if len(key) != self.step_size or not isinstance(key, tuple):
            raise TypeError(
                "Type must be of the same length as step_size and must be a tuple")
        if key not in self.chain.keys():
            raise KeyError("Item is not found in this chain")
        self.current_state = state

    def random_state(self):
        """Returns a random seed from the chain and also sets the seed"""
        self.current_state = r.choice(list(self.chain.keys()))
        return self.current_state

    def predict(self, n):
        return list(toolz.itertoolz.take(n, self))

