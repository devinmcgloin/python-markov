import random as r
import toolz


class markov_chain:
    """Simple Markov Chain designed for small datasets and experimentation"""

    def __init__(self, iterable, step_size=1):
        iterator = iter(iterable)
        current_window = []
        self.chain = {}
        self.step_size = step_size
        for i in range(step_size):
            current_window.append(next(iterator))
        next_item = next(iterator)
        while True:
            window = tuple(current_window)
            if window in self.chain.keys():
                self.chain[window].append(next_item)
            else:
                self.chain[tuple(current_window)] = [next_item]
            current_window.pop(0)
            current_window.append(next_item)
            try:
                next_item = next(iterator)
            except StopIteration:
                break
        self.current_state = r.choice(list(self.chain.keys()))

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
        if len(key) != self.step_size or not isinstance(key, tuple):
            raise TypeError("Type must be of the same length as step_size and must be a tuple")
        if key not in self.chain.keys():
            raise KeyError("Item is not found in this chain")
        options = self.chain[key]
        return r.choice(options)

    def __setitem__(self, key, value):
        """Adds possible outcome to the given key"""
        if len(key) != self.step_size or not isinstance(key, tuple):
            raise TypeError("Type must be of the same length as step_size and must be a tuple")
        if key in self.chain.keys():
            self.chain[key].append(value)
        else:
            self.chain[key] = [value]

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
        self.current_state = state

    def random_state(self):
        """Returns a random seed from the chain and also sets the seed"""
        self.current_state = r.choice(list(self.chain.keys()))
        return self.current_state

    def predict(self, n):
        return list(toolz.itertoolz.take(n, self))
