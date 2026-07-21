# BRUTE FORCE
# Time: O(n²)  Space: O(n)

def mergeIntervals_brute():
    intervals = [[1, 3], [2, 4], [6, 8], [9, 10]]

    intervals.sort()
    result = []

    for i in range(len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]

        if result and result[-1][1] >= end:
            continue

        for j in range(i + 1, len(intervals)):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])

        result.append([start, end])

    print(f"Brute Force Result: {result}")

mergeIntervals_brute()