import markov_simple as ms

class markov_text(ms.markov_chain):

    def __init__(self, iterable, step_size=1):
        super(markov_text, self).__init__(iterable, step_size)

mar = markov_text(["a","b","c"])
print(mar)
mar.predict(10)

