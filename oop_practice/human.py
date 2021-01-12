from abc import ABC, abstractmethod


class Human(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError
        
