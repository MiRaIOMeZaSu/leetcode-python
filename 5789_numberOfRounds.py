class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start = startTime.split(":")
        finish = finishTime.split(":")
        h_start = int(start[0])
        h_finish = int(finish[0])
        m_start = int(start[1])
        m_finish = int(finish[1])
        if m_start % 15 != 0:
            m_start = (m_start // 15) * 15 + 15
        if m_finish % 15 != 0:
            m_finish = (m_finish // 15) * 15
        # 开始计算间隔
        h_gap = 0
        if h_start > h_finish or (h_start == h_finish and m_start > m_finish):
            h_gap += 24 - h_start
            h_start = 0
        h_gap += h_finish - h_start
        ret = 0
        ret += h_gap * 4
        ret += (m_finish - m_start) // 15
        return ret


if __name__ == "__main__":
    ret = Solution().numberOfRounds("00:01",
                                    "00:00")
    print(ret)
