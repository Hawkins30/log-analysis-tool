def count_levels(entries, filter_level=None):
    counts = {}

    for entry in entries:
        level = entry["level"]

        if filter_level and level != filter_level:
            continue

        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1

    return counts
