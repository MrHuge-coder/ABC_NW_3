import enum


class ShipType(enum.Enum):
    liner = 1
    tug = 2
    tanker = 3

    @staticmethod
    def get(k):
        if k == 1:
            return ShipType.liner
        elif k == 2:
            return ShipType.tug
        elif k == 3:
            return ShipType.tanker
        return Exception
