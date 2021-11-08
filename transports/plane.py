from transports.baseTransport.inOutAble import InOutInterface
from transports.baseTransport.transport import Transport


class Plane(InOutInterface, Transport):
    def __init__(self):
        super().__init__()
        self.max_distance = None
        self.max_weight = None

    def input_pl(self, file):
        split_data = list(map(int, file.readline().split(' ')))
        self.max_distance = split_data[0]
        self.max_weight = split_data[1]
        self.speed = split_data[2]
        self.distention = split_data[3]
        self.perfectTime = self.perfect_time()

    def in_rnd(self):
        self.max_distance = Transport.rnd20.get()
        self.max_weight = Transport.rnd20.get()
        self.speed = Transport.rnd20.get()
        self.distention = Transport.rnd20.get()
        self.perfectTime = self.perfect_time()

    def out(self, file):
        file.write("""It is Plane: \
                max distance = {}, \
                max weight = {}, \
                speed = {}, \
                distention = {}\
                Perfect Time = {}\n"""
                   .format(self.max_distance, self.max_weight, self.speed,
                           self.distention, self.perfectTime))
