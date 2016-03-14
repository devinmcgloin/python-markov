from collections import Counter

def get_probabilites(windows):
    probs = {}
    for key, val in windows.items():
        val_counts = Counter(val)
        total = len(val)
        probabilities = []
        for item in val_counts:
            probabilities.append((val[0], val_counts[val[0]] / total))
        probs[key] = probabilities
    return probs

