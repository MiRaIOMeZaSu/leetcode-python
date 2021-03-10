class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        routes = []
        self.tree(routes, [], nums)
        return routes

    def tree(self, routes, route, nums):
        """
        :type nums: List[int]
        :type route: List[int]
        :rtype: List[int]
        """
        if len(route) == len(nums):
            routes.append(route)
            return

        for num in nums:
            if num in route:
                continue
            route.append(num)
            self.tree(routes, route[:], nums)
            route.remove(num)


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([0, 1]))
