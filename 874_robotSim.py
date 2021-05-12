from typing import List
import bisect


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x_obstacles = {}
        y_obstacles = {}
        for pos in obstacles:
            x_obstacles.setdefault(pos[0], [])
            y_obstacles.setdefault(pos[1], [])
            x_obstacles[pos[0]].append(pos[1])
            y_obstacles[pos[1]].append(pos[0])
        # 存储当前方向
        for key in x_obstacles.keys():
            x_obstacles[key].sort()
        for key in y_obstacles.keys():
            y_obstacles[key].sort()
        direction = 0
        currPos = [0, 0]
        directions = [0, 1, 2, 3]
        # 北, 东, 南, 西
        # 0, 1, 2, 3
        x_direction = set([1, 3])
        y_direction = set([0, 2])
        # 0, 2   1, 3
        changeDirection = set([-1, -2])
        ret = 0
        for command in commands:
            if command in changeDirection:
                if command == -1:
                    direction += 1
                else:
                    direction -= 1
                if direction < 0:
                    direction += 4
                elif direction > 3:
                    direction -= 4
            elif directions[direction] in x_direction:
                # 此时在x轴方向上移动, y值时固定的
                theObstacles = y_obstacles[currPos[1]
                                           ] if currPos[1] in y_obstacles else []
                if directions[direction] == 1:
                    # 方向为正
                    # 往左寻找
                    index = bisect.bisect_right(theObstacles, currPos[0])
                    if theObstacles and len(theObstacles) != index and theObstacles[index] <= currPos[0] + command:
                        # 此时被阻挡
                        currPos[0] = theObstacles[index] - 1
                    else:
                        currPos[0] += command
                else:
                    # 方向为负
                    # 往右寻找
                    index = bisect.bisect_left(theObstacles, currPos[0])
                    if theObstacles and index != 0 and theObstacles[index - 1] >= currPos[0] - command:
                        # 此时被阻挡
                        currPos[0] = theObstacles[index - 1] + 1
                    else:
                        currPos[0] -= command
                ret = max(currPos[0] ** 2 + currPos[1]**2, ret)
            elif directions[direction] in y_direction:
                theObstacles = x_obstacles[currPos[0]
                                           ] if currPos[0] in x_obstacles else []
                if directions[direction] == 0:
                    # 方向为正
                    index = bisect.bisect_right(theObstacles, currPos[1])
                    if theObstacles and len(theObstacles) != index and theObstacles[index] <= currPos[1] + command:
                        # 此时被阻挡
                        currPos[1] = theObstacles[index] - 1
                    else:
                        currPos[1] += command
                else:
                    index = bisect.bisect_left(theObstacles, currPos[1])
                    if theObstacles and index != 0 and theObstacles[index - 1] >= currPos[1] - command:
                        # 此时被阻挡
                        currPos[1] = theObstacles[index - 1] + 1
                    else:
                        currPos[1] -= command
                ret = max(currPos[0] ** 2 + currPos[1]**2, ret)
        return ret


if __name__ == "__main__":
    ret = Solution().robotSim()
    print(ret)
