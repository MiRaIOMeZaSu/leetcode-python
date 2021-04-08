class Foo:
    def __init__(self):
        self.flag = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while(self.flag != 1):
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while(self.flag != 2):
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
