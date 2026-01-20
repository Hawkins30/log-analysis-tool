def parse_log_file(path, valid_levels, filter_level=None):
    entries = []
    malformed_count = 0

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(" ")

            if len(parts) < 4:
                malformed_count += 1
                continue

            level = parts[2]

            if level not in valid_levels:
                malformed_count += 1
                continue

            if filter_level and level != filter_level:
                continue

            entries.append(level)

    return entries, malformed_count
