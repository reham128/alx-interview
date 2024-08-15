#!/usr/bin/python3
import sys
import signal


total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def signal_handler(sig, frame):
    """Handle keyboard interrupt."""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    line_count += 1

    parts = line.strip().split()
    if len(parts) != 10 or parts[1] != '-' or parts[3] != 'GET'
    or parts[6] != 'HTTP/1.1':
        continue

    try:
        status_code = int(parts[7])
        file_size = int(parts[8])
    except (ValueError, IndexError):
        continue

    total_file_size += file_size
    if status_code in status_codes:
        status_codes[status_code] += 1

    if line_count % 10 == 0:
        print_statistics()

