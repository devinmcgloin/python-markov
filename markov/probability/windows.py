import collections

def get_windows(iterator, step_size):
    """Given an iterator get windows calculates
    tuples of size step_size, and pairs them with
    the next item in a dictionary """
    current_window = []
    counts = {}
    for i in range(step_size):
        current_window.append(next(iterator))
    next_item = next(iterator)
    while True:
        window = tuple(current_window)
        if window in counts.keys():
            counts[window].append(next_item)
        else:
            counts[window] = [next_item]
        current_window.pop(0)
        current_window.append(next_item)
        try:
            next_item = next(iterator)
        except StopIteration:
            break
    return counts

