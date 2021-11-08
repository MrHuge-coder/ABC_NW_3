from helpers.shipType import ShipType
from transports.baseTransport.inOutAble import InOutInterface
from transports.baseTransport.transport import Transport


class Ship(InOutInterface, Transport):
    def __init__(self):
        super().__init__()
        self.type = None
        self.displacement = None

    def input_pl(self, file):
        split_data = list(map(int, file.readline().split(' ')))
        self.displacement = split_data[0]
        self.type = ShipType.get(int(split_data[1]))
        self.speed = split_data[2]
        self.distention = split_data[3]
        self.perfectTime = self.perfect_time()

    def in_rnd(self):
        self.displacement = Transport.rnd20.get()
        self.type = ShipType.get(int(Transport.rnd20.get() % 3 // 1 + 1))
        self.speed = Transport.rnd20.get()
        self.distention = Transport.rnd20.get()
        self.perfectTime = self.perfect_time()

    def out(self, file):
        file.write("""It is Ship: displacement = {}\
            Ship Type - {}\
            speed = {}\
            distention = {}\
            Perfect Time = {}\n"""
                   .format(self.displacement, self.type.name,
                           self.speed, self.distention, self.perfectTime))
