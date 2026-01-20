import argparse
from parser import parse_log_file
from analyser import count_levels
from reporter import print_report, write_csv, write_json

def main():
    parser = argparse.ArgumentParser(description="Log analysis tool")
    parser.add_argument("--level", help="Filter by log level (ERROR, WARNING, INFO)")
    parser.add_argument("--output", help="Output CSV file")
    parser.add_argument("--json", help="Output JSON file")
    args = parser.parse_args()

    log_file_path = "sample_logs/example.log"
    valid_levels = ["ERROR", "WARNING", "INFO"]

    entries, malformed_count = parse_log_file(
        log_file_path,
        valid_levels,
        filter_level=args.level
    )

    level_counts = count_levels(entries)
    total_valid = sum(level_counts.values())
    error_count = level_counts.get("ERROR", 0)

    if total_valid > 0:
        error_percentage = (error_count / total_valid) * 100
    else:
        error_percentage = 0

    if args.json:
        write_json(level_counts, args.json)
        print("JSON report written to", args.json)
    elif args.output:
        write_csv(level_counts, args.output)
        print("CSV report written to", args.output)
    else:
        print_report(level_counts)

        print()
        print("Summary:")
        print("Total valid entried:", total_valid)
        print("Malformed lines skipped:", malformed_count)
        print("ERROR percentage:", round(error_percentage, 1), "%")

main()
