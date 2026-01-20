def output_results(counts, output_file=None):
    if output_file:
        with open(output_file, "w") as file:
            file.write("level,count\n")
            for level in counts:
                file.write(level + "," + str(counts[level]) + "\n")

        print("Report written to", output_file)
    else:
        print("Log level counts:")
        for level in counts:
            print(level, ":", counts[level])
