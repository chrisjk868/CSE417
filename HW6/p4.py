def find_kth_largest(nums, k):
    k = len(nums) - k
    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: return quick_select(l, p - 1)
        elif p < k: return quick_select(p + 1, r)
        else: return nums[p]

    return quick_select(0, len(nums) - 1)

nums = [1, 34, 5, 6, 2, 7, 4]
k = 3
print("Input numsay: ", nums)
print(f'Sorted: {sorted(nums)}')
print(f"{k}-th largest element: ", find_kth_largest(nums, k))