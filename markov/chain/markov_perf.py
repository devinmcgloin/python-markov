import random as r
import toolz


class markov_perf:
    """Performant Markov change to be used with large datasets"""

    def __init__(self, iterable, step_size=1):
        iterator = iter(iterable)
        current_window = []
        self.chain = {}

    def __str__(self):
        """Display Chain Structure"""
        string = ""
        for key, val in self.chain.items():
            string += "{key:-<40}{val:->40} \n".format(key=str(key), val=str(val))
        return string

    def __len__(self):
        """Returns the total number of links in the chain"""
        return len(self.chain)

    def __getitem__(self, key):
        """Gets the next prediction given the input key"""
        if key not in self.chain.keys():
            raise KeyError("Item is not found in this chain")

    def __iter__(self):
        """Iterates over the chain yeilding values based on seed"""
        return self

    def __next__(self):
        try:
            next_item = self[self.current_state]
        except KeyError:
            raise StopIteration

    def __contains__(self, item):
        """"Returns true if item is a link in the chain"""
        return item in self.chain.keys()

    def set_state(self, state):
        """Defines the seed to be used while iterating over the chain. Seed only determines the start value,
        not the subsequent values."""
        self.current_state = state

    def random_state(self):
        """Returns a random seed from the chain and also sets the seed"""
        self.current_state = r.choice(list(self.chain.keys()))
        return self.current_state

    def predict(self, n):
        return list(toolz.itertoolz.take(n, self))

    def write_to_disk(self, path):
        """Takes file path and writes to file"""
        pass

    def read_from_disk(self, path):
        """Takes file path and reads in to the chain.
        Overwrites content currently in the chain"""
        pass

