#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys
import re

total = 0

pat = r'^([\d]{1,3}\.){3}([\d]{1,3})'
pat += r'( - )(\[[\d]{4}-[\d]{2}-[\d]{2}'
pat += r' [\d]{2}:[\d]{2}:[\d]{2}\.[\d]{1,}\])'
pat += r'( "GET \/projects\/260 HTTP\/1\.1") '
pat += r'([\d]{3}) ([\d]{1,4})$'


codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

line = 0


def valid(line: str) -> bool:
    result = re.match(pat, line)
    if result:
        return True
    return False


def generate_statistics(line: str) -> None:
    global total
    chars = line.split(' ')

    size = int(chars[-1].replace('\n', ''))
    try:
        status_code = int(chars[-2])
        if status_code in codes:
            codes[status_code] += 1
    except ValueError:
        pass

    total += size


def print_statistics() -> None:
    print('File size: {}'.format(total))
    for key, value in sorted(codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    try:
        for i, line in enumerate(sys.stdin, 1):
            # generate statistics only for a valid log
            if valid(line):
                generate_statistics(line)
            if not i % 10:
                print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise
