# OPTIMAL
# Time: O(n log n)  Space: O(n)

def mergeIntervals_optimal():
    intervals = [[1, 3], [2, 4], [6, 8], [9, 10]]

    intervals.sort()
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        last = result[-1]
        curr = intervals[i]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            result.append(curr)

    print(f"Optimal Result: {result}")

mergeIntervals_optimal()