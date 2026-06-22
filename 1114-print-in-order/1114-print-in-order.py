import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Lock()
        self.second_done = threading.Lock()
        
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
