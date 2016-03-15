import jsonpickle

# import markov.chain.markov_simple as ms
# import markov.chain.markov_text as mt
# import markov.chain.markov_perf as mp

from markov.chain.markov_simple import markov_chain
from markov.chain.markov_text import markov_text
from markov.chain.markov_perf import markov_perf


def write_to_disk(chain, path):
    """Takes file path and writes to file"""
    d = {}
    d["object"] = type(chain)
    d["step_size"] = chain.step_size
    d["current_state"] = chain.current_state
    d["chain"] = chain.chain
    
    item = jsonpickle.encode(d, keys=False)
    
    with open(path, "w") as f:
        f.write(item)


def read_from_disk(path):
    """Takes file path and reads in to the chain.
    Overwrites content currently in the chain"""
    with open(path, "r") as f:
        item = f.read()
    d = jsonpickle.decode(item, keys=False)
    if d["object"] == markov_perf:
        chain = markov_perf(d["step_size"], d["current_state"], d["chain"])
    elif d["object"] == markov_text:
        chain = markov_text("")
    else:
        chain = markov_simple("")
    return chain
