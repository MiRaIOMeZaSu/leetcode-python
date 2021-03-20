# 冒泡排序:每次将最大数放到最后面
info = [int(i) for i in input().split()]
nums = []
for i in range(info[0]):
    nums.append(int(input()))
# 数据收取完毕
count = 0
_sum = 0
for i in range(0, info[0]):
    num = nums[0]
    for n in range(1, info[0] - count):
        if(num > nums[n]):
            # 目标应该前进
            nums[n - 1] = nums[n]
        else:
            nums[n - 1] = num
            num = nums[n]
    nums[info[0] - count - 1] = num
    count += 1
    _sum += nums[info[0] - count]
    if(_sum >= info[1]):
        break
print(count)
