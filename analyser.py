def count_levels(entries):
    counts = {}

    for level in entries:
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1

    return counts
