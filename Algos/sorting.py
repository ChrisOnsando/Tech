array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]


def bubble_sort(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]


print(array)
bubble_sort(array)
print(array)

array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]


def insertion_sort(nums: list):
    for i in range(1, len(nums), +1):
        curr: int = nums[i]
        pos: int = i
        while pos > 0 and nums[pos - 1] > curr:
            nums[pos] = nums[pos - 1]
            pos -= 1
        nums[pos] = curr


print(array)
insertion_sort(array)
print(array)