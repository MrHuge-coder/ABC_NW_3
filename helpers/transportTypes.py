import enum


class TransportTypes(enum.Enum):
    Ship = 1
    Train = 2
    Plane = 3

    @staticmethod
    def get(k):
        if k == 1:
            return TransportTypes.Ship
        elif k == 2:
            return TransportTypes.Train
        elif k == 3:
            return TransportTypes.Plane
        return Exception

    def get_class(self):
        if self == TransportTypes.Ship:
            from transports.ship import Ship
            return Ship
        elif self == TransportTypes.Train:
            from transports.train import Train
            return Train
        elif self == TransportTypes.Plane:
            from transports.plane import Plane
            return Plane
