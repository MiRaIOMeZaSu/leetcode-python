import math
size = int(input())
nums = [int(i) for i in input().split()]
bucketSize = math.ceil(1000 / size)
ret = []
buckets = [[] for i in range(0, size)]
for i in nums:
    time = 1
    while(time * bucketSize < 1001):
        if(i <= time * bucketSize):
            buckets[time - 1].append(i)
            break
        time += 1
for bucket in buckets:
    temp = list(set(bucket))
    temp.sort()
    for i in temp:
        ret.append(i)
print(len(ret))
for i in ret:
    print(str(i) + ' ', end='')
