from collections import Counter

def get_probabilites(windows):
    probs = {}
    for key, val in windows.items():
        val_counts = Counter(val)
        total = len(val)
        probabilities = []
        for item in val_counts:
            probabilities.append((item, val_counts[item] / total))
        probs[key] = probabilities
    return probs

