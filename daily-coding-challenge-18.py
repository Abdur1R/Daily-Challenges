"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import itertools

def minimum_rooms(lectures):
    input_data = [' '.join(str(j) for j in i) for i in lectures]
    combinations = set()
    rooms = 0
    for c in itertools.combinations(input_data, 2):
        a = set(range(*(int(n) for n in c[0].split())))
        b = set(range(*(int(i) for i in c[1].split())))
        if not a.intersection(b) == set():
            rooms += 1
    return rooms if rooms > 0 else 1

if __name__ == "__main__":
    # Read the number of lines to read
    rows = int(input())
    lectures = []
    for i in range(rows):
        lectures.append([int(n) for n in input().split()])
    print(minimum_rooms(lectures))
    