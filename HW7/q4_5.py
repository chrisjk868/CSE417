import random

def interval_generator(n, L, r, v):
    intervals = []
    for i in range(n):
        start = random.randint(1, L)
        length = random.randint(1, r)
        value = random.randint(1, v)
        intervals.append((start, start + length, value))
    return intervals

def greedy_earliest(intervals):
    # Sort by end time in ascending order
    intervals.sort(key=lambda x:x[1])
    selected = []
    end = 0
    weight = 0
    for s, f, w in intervals:
        if end >= s:
            continue
        weight += w
        selected.append((s, f, w))
        end = f
    return weight, selected

def greedy_maxval(intervals):
    # Sort by weight in descending order
    intervals.sort(key=lambda x:x[-1], reverse=True)
    selected = []
    end = 0
    weight = 0
    for s, f, w in intervals:
        if end >= s:
            continue
        weight += w
        selected.append((s, f, w))
        end = f
    return weight, selected

def greedy_val_density(intervals):
    # Sort by density in descending order
    density_intervals = [(s, f, w, (w / (f - s))) for s, f, w in intervals]
    density_intervals.sort(key=lambda x:x[-1], reverse=True)
    selected = []
    end = 0
    weight = 0
    for s, f, w, d in density_intervals:
        if end >= s:
            continue
        weight += w
        selected.append((s, f, w, d))
        end = f
    return weight, selected


def find_max_weight_intervals(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    # Initialize memo table with 0 values
    memo = [0] * len(intervals)
    # Compute maximum weight for each interval
    for i in range(len(intervals)):
        # Compute maximum weight for intervals before the current interval
        for j in range(i):
            if intervals[j][1] <= intervals[i][0]:
                memo[i] = max(memo[i], memo[j])
        # Add the current interval's weight to the maximum weight found so far
        memo[i] += intervals[i][2]
    # Find the maximum weight in the memo table
    max_weight = max(memo)
    # Find the selected intervals that contribute to the maximum weight
    selected_intervals = []
    current_weight = max_weight
    for i in range(len(intervals)-1, -1, -1):
        if current_weight == 0:
            break
        if memo[i] == current_weight:
            selected_intervals.append(intervals[i])
            current_weight -= intervals[i][2]
    # Reverse the selected intervals list to get them in chronological order
    selected_intervals.reverse()
    # Return the maximum weight and the selected intervals
    return (max_weight, selected_intervals)

for i in range(10):
    intervals = interval_generator(10_000, 1_000_000, 2000, 100)
    a = greedy_earliest(intervals)
    b = greedy_maxval(intervals)
    c = greedy_val_density(intervals)
    d = find_max_weight_intervals(intervals)

    print(f'{a[0]}, {len(a[1])}, {b[0]}, {len(b[1])}, {c[0]}, {len(c[1])}, {d[0]}, {len(d[1])}')