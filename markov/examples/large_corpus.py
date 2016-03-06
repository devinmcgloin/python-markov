from markov.chain.markov_simple import markov_chain

text = []
with open("data/sawyer.txt", "r") as f:
    for index, line in enumerate(f):
        if 482 < index < 8863:
            text.append(line)

text = "".join(text).split()

chain = markov_chain(text, 1)
chain.random_state()
print(" ".join(chain.predict(100)))
