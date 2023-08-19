import random

comparisons = 0

def find_kth_largest(nums, k):
    k = len(nums) - k
    def quick_select(l, r):
        global comparisons
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                comparisons += 1
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: 
            return quick_select(l, p - 1)
        elif p < k:
            return quick_select(p + 1, r)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)

def generate_random_array(n):
    """
    Returns an array of n random integers between 0 and 100.
    """
    arr = [random.randint(0, n) for _ in range(n)]
    return arr

for n in range(50000, 500001, 50000):
    find_kth_largest(generate_random_array(n), n // 2)
    print(f'{n}, {comparisons}')
    comparisons = 0