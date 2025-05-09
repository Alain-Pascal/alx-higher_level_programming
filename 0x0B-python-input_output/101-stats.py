#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""
import sys
from collections import defaultdict


def main():
    """
    Reads stdin line by line, computes metrics, and prints statistics
    """

    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_parts = line.split()

            # validate line format
            if len(line_parts) >= 2:  # minimum length of a valid line
                try:
                    # attempt to parse status code and file size
                    file_size = int(line_parts[-1])
                    status_code = int(line_parts[-2])

                    # update metrics
                    total_file_size += file_size
                    status_code_counts[status_code] += 1
                except (ValueError, IndexError):
                    # skip lines with invalid format
                    continue

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)
        raise

    print_stats(total_file_size, status_code_counts)  # final print


def print_stats(total_file_size, status_code_counts):
    """
    Prints the computed statistics

    Args:
        total_file_size (int): total file size
        status_code_counts (dict): a dictionary of status code counts
    """

    print("File size: {}".format(total_file_size))

    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))


if __name__ == "__main__":
    main()
