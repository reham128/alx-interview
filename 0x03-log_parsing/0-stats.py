#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = {200: 0,
                    301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 7:
                try:
                    ip_address = parts[0]
                    date = parts[2][1:]  # remove the leading '['
                    request = parts[3]  # GET
                    status_code = int(parts[5])  # status code
                    file_size = int(parts[6])  # file size

                    if status_code in status_codes:
                        total_size += file_size
                        status_codes[status_code] += 1

                except (ValueError, IndexError):
                    continue

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
