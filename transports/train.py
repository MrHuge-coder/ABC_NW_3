from transports.baseTransport.inOutAble import InOutInterface
from transports.baseTransport.transport import Transport


class Train(InOutInterface, Transport):
    def __init__(self):
        super().__init__()
        self.count_carriage = None

    def input_pl(self, file):
        split_data = list(map(int, file.readline().split(' ')))
        self.count_carriage = split_data[0]
        self.speed = split_data[1]
        self.distention = split_data[2]
        self.perfectTime = self.perfect_time()

    def in_rnd(self):
        self.count_carriage = Transport.rnd20.get()
        self.speed = Transport.rnd20.get()
        self.distention = Transport.rnd20.get()
        self.perfectTime = self.perfect_time()

    def out(self, file):
        file.write("""It is Train: \
                    count of carriage = {} \
                    speed = {} \
                    distention = {}\
                    Perfect time = {}\n""".format(self.count_carriage, self.speed, self.distention, self.perfectTime))
