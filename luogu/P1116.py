# 使用冒泡
size = int(input())


def sort(nums, size):
    times = 0
    for i in range(0, size):
        for n in range(i + 1, size):
            if(nums[i] > nums[n]):
                times += 1
    return times


times = 0
nums = []
while(size - len(nums) != 0):
    nums.extend([int(i) for i in input().split()])

if(len(nums) > 0):
    times = sort(nums, size)
print(times)
