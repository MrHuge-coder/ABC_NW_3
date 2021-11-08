from helpers.randomData import RandomData
from transports.baseTransport.inOutAble import InOutInterface
from transports.baseTransport.transport import Transport


class Container(InOutInterface):
    def __init__(self):
        self.len = 0
        self.storage = []
        self.size = 0

    def __del__(self):
        self.__clear()

    def out(self, file):
        file.write("container contains {} elements.\n".format(self.len))
        for i in range(len(self.storage)):
            file.write("{}: ".format(i))
            self.storage[i].out(file)

    def input_pl(self, file):
        iterator = True
        k = file.readline()
        if not k:
            iterator = False
        while iterator:
            self.storage.append(Transport.static_in(file, int(k)))
            self.len += 1
            k = file.readline()
            if not k:
                iterator = False

    def in_rnd(self):
        a = RandomData(10000, 10000000).get()
        print(a)
        if a > self.size:
            self.size = a
        while self.len < a:
            self.storage.append(Transport.static_in_rnd())
            self.len += 1

    def in_rnd_count(self, s):
        if s > self.size:
            self.size = s
        while self.len < s:
            self.storage.append(Transport.static_in_rnd())
            self.len += 1

    def shaker_sort(self):
        def swap(i, j):
            self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

        upper = self.len - 1
        lower = 0
        no_swap = False
        while not no_swap and upper - lower > 1:
            no_swap = True
            for j in range(lower, upper):
                if self.storage[j + 1].perfectTime < self.storage[j].perfectTime:
                    swap(j + 1, j)
                    no_swap = False
            upper = upper - 1
            for j in range(upper, lower, -1):
                if self.storage[j - 1].perfectTime > self.storage[j].perfectTime:
                    swap(j - 1, j)
                    no_swap = False
            lower = lower + 1

    def __clear(self):
        self.storage.clear()
        self.len = 0
