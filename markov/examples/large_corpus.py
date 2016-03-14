from markov.chain.markov_simple import markov_chain
from markov.chain.markov_text import markov_text

text = []
with open("data/sawyer.txt", "r") as f:
    for index, line in enumerate(f):
        if 482 < index < 8863:
            text.append(line)

text = "".join(text).split()

chain = markov_chain(text, 1)
chain.random_state()
print("Normal Chain Predictions: ")
print(chain.predict(100))

chain_text = markov_text(text,1)
chain_text.random_state()
print("Text Chain Predictions: ")
print(chain_text.predict(100))


