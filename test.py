

def quick_sort(nums):
    def part(nums, low_num, high_num):
        mean = nums[(low_num + high_num) // 2]
        mn = low_num - 1
        mx = high_num + 1
        while True:
            mn += 1
            while nums[mn] < mean:
                mn += 1
            mx -= 1
            while nums[mx] > mean:
                mx -= 1
            if mn >= mx:
                return mx
            nums[mn], nums[mx] = nums[mx], nums[mn]

    def _quick_sort(numbers, low_num, high_num):
        if low_num < high_num:
            sep_ind = part(numbers, low_num, high_num)
            _quick_sort(numbers, low_num, sep_ind)
            _quick_sort(numbers, sep_ind + 1, high_num)
    _quick_sort(nums, 0, len(nums) - 1)

nums = [11, 3, 6, 1246, 67, 99, 3467, 4214, 67, 0, 145, 6]
quick_sort(nums)
print(nums)