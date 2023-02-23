#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys

count = 0
tot = 0
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for lines in sys.stdin:
        llist = lines.split(" ")
        if len(llist) > 4:
            code = llist[-2]
            size = int(llist[-1])
            if code in cache.keys():
                cache[code] += 1
            tot += size
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(tot))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(tot))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))