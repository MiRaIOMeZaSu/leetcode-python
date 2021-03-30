# 获取所有排序可能,再寻找满足条件的答案
# 1-9
# 回溯法+集合


def solve(nums: list, ret=[], result=[]):
    # for i in nums:
    for i in nums:
        newNums = [x for x in nums]
        newNums.remove(i)
        ret.append(i)
        if(len(ret) == 6):
            if((ret[0] * 100 + ret[1] * 10 + ret[2]) * 2 == (ret[3] * 100 + ret[4] * 10 + ret[5])):
                pass
            else:
                ret.remove(i)
                continue
        solve(newNums, ret, result)
        if(len(ret) == 9):
            if((ret[0] * 100 + ret[1] * 10 + ret[2]) * 3 == (ret[6] * 100 + ret[7] * 10 + ret[8])):
                a = ret[0] * 100 + ret[1] * 10 + ret[2]
                result.append("{} {} {}".format(a, a * 2, a * 3))
        ret.remove(i)


if __name__ == "__main__":
    nums = []
    for i in range(1, 10):
        nums.append(i)
    # 集合初始化完毕
    result = []
    solve(nums, result=result)
    for i in result:
        print(i)
