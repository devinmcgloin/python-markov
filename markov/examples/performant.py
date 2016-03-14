from markov.chain.markov_perf import markov_perf


text = []
with open("data/sawyer.txt", "r") as f:
    for index, line in enumerate(f):
        if 482 < index < 8863:
            text.append(line)

text = "".join(text).split()

chain = markov_perf(text, 1)
chain.random_state()
print("Performat Chain Predictions: ")
print(chain.predict(100))
