#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """Prints statistics based on the computed metrics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def compute_metrics():
    """Reads stdin line by line and computes metrics."""
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            if len(parts) > 2:
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
