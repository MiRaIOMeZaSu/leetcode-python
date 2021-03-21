# 使用快排
size = int(input())


times = 0


def quickSort(nums, left, right):
    if(left < 0 or right >= len(nums)):
        return
    if(right <= left):
        return
    patitationIndex = sort(nums, left, right)
    quickSort(nums, left, patitationIndex - 1)
    quickSort(nums, patitationIndex + 1, right)


def sort(nums, left, right):
    global times
    pivot = left
    index = i = left + 1
    while(i <= right):
        if(nums[index] <= nums[pivot]):
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            if(i - index <= 1):
                times += i - index
            else:
                times += 2 * (i - index) - 1
            index += 1
        i += 1

    temp = nums[pivot]
    nums[pivot] = nums[index - 1]
    nums[index - 1] = temp
    if(index - 1 - pivot <= 1):
        times += index - 1 - pivot
    else:
        times += 2 * (index - 1 - pivot) - 1
    return index - 1


if size > 0:
    nums = [int(i) for i in input().split()]
    quickSort(nums, 0, size - 1)
print(times)
