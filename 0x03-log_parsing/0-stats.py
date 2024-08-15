#!/usr/bin/python3
import sys
import signal


status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_size = 0
line_count = 0


def print_stats():
    """
    Function to print the total file size and the count of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def handle_signal(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 7:
            continue

        ip = parts[0]
        # parts[1] is '-'
        # parts[2] is the date within brackets
        method = parts[3][1:]  # "GET
        resource = parts[4]  # /projects/260
        protocol = parts[5][:-1]  # HTTP/1.1"
        status_code = parts[6]
        try:
            file_size = int(parts[7])
        except ValueError:
            continue

        total_size += file_size
        line_count += 1

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        if line_count % 10 == 0:
            print_stats()


except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
