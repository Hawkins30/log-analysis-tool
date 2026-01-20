import argparse
from parser import parse_log_file
from analyser import count_levels
from reporter import output_results

def main():
    parser = argparse.ArgumentParser(description="Log analysis tool")
    parser.add_argument("--level", help="Filter by log level (ERROR, WARNING, INFO)")
    parser.add_argument("--output", help="Output CSV file")
    args = parser.parse_args()

    log_file_path = "sample_logs/example.log"
    valid_levels = ["ERROR", "WARNING", "INFO"]

    entries = parse_log_file(log_file_path, valid_levels)
    counts = count_levels(entries, args.level)
    output_results(counts, args.output)

main()
