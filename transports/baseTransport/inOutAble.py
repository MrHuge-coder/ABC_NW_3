from abc import ABCMeta, abstractmethod


class InOutInterface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def out(self, file):
        pass

    @abstractmethod
    def input_pl(self, file):
        pass

    @abstractmethod
    def in_rnd(self):
        pass
