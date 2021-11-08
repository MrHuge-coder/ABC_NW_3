from helpers.randomData import RandomData
from helpers.transportTypes import TransportTypes


class Transport:
    rnd20 = RandomData(1, 20)
    rnd3 = RandomData(1, 3)

    def __init__(self):
        self.perfectTime = None
        self.speed = None
        self.distention = None

    # -----------------------------------------------
    # Ввод параметров обобщенной транспорта из файла
    @staticmethod
    def static_in(file, k):
        sp = TransportTypes.get(k).get_class()
        sp.input_pl(file)
        return sp

    # -----------------------------------------------
    # Случайный ввод обобщенного транспорта
    @staticmethod
    def static_in_rnd():
        k = Transport.rnd3.get()
        sp = TransportTypes.get(k).get_class()()
        sp.in_rnd()
        return sp

    # -----------------------------------------------
    # Вычисление идеального времени прохождения
    # расстояния для  обобщенного транспорта
    def perfect_time(self):
        return self.distention / self.speed
