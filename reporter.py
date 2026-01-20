import json

def print_report(level_counts):
    print("Log level counts:")
    for level in level_counts:
        print(level, ":", level_counts[level])

def write_csv(level_counts, output_path):
    with open(output_path, "w") as output_file:
        output_file.write("level,count\n")
        for level in level_counts:
            output_file.write(level + "," + str(level_counts[level]) + "\n")

def write_json(level_counts, output_path):
    with open(output_path, "w") as output_file:
        json.dump(level_counts, output_file, indent=2)

