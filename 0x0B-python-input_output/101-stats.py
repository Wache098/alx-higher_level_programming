#!/usr/bin/python3
"""Module containing a script that reads stdin line by line and computes,
metrics
Each 10 lines and after a keyboard interruption (CTRL + C), prints those,
statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""


import sys

def print_statistics(file_size, status_tally):
    """Prints the computed statistics."""
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for i, line in enumerate(sys.stdin, start=1):
        tokens = line.split()
        if len(tokens) >= 2 and tokens[-2] in status_tally:
            status_tally[tokens[-2]] += 1
        try:
            file_size += int(tokens[-1])
        except Exception:
            pass
        if i % 10 == 0:
            print_statistics(file_size, status_tally)

    print_statistics(file_size, status_tally)

except KeyboardInterrupt:
    print_statistics(file_size, status_tally)
