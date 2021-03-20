class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.map = dict()

    def add(self, number):
        # write your code here
        if(number not in self.map):
            self.map[number] = 1
            return
        self.map[number] += 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for key in self.map.keys():
            other = value - key
            if(other in self.map):
                if(other * 2 == value):
                    return False if self.map[other] == 1 else True
                return True
        return False


if __name__ == "__main__":
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    twoSum.find(4)
    twoSum.find(7)
