from human import Human
import random
from random import randrange

class Person(Human):

    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    def __str__(self):
        if self.home:
            return f'My name is {self.name}. I`\m {self.age} years old. I have home. My budget is {self.money}'
        return f'My name is {self.name}. I`\m {self.age} years old. I dont have home. money: {self.money}'

    def make_money(self):
        salary = randrange(1000, 1500)
        self.money += salary

    def working(self, number_of_months):
        list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        num_month = 0
        for _ in range(number_of_months):
            self.make_money()
            print(f'{self.name} go to work and get the salary of {list_of_months[num_month]}, cash: {self.money}')
            if num_month == 11:
                num_month = 0
            else:
                num_month += 1

    def buy_house(self):
        print(f'{self.name} has enough money to buy house!')


class RieltorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Rieltor(metaclass=RieltorMetaClass):

    def __init__(self, name, list_houses):
        self.name = name
        self.list_houses = list_houses
        self.discount = randrange(0, 10)

    def info_houses(self):
        return f'My name is {self.name}. I`m rieltor. This is my catalog of houses {self.list_houses}.\nI could provide you {self.discount}% discount if u buy from me.'

    def sell_house(self, house):
        choice = randrange(1, 10)
        if choice == 1:
            print(f'{self.name} steal client money and didin`t sell house!')
            return False
        self.list_houses.remove(house)
        return True


class House:

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def __repr__(self):
        return f'House has {self.area} m2 and price is {self.cost}'


def sell_house(rieltor, person, house):
    price = int(house.cost * (1 - rieltor.discount / 100))
    if rieltor.sell_house(house):
        person.money -= price
        person.home = True
        print(f'{rieltor.name} sell a new house {person.name} with {house.area} m2 and it`s cost {house.cost}.')


if __name__ == '__main__':
    # 1. create persons.
    list_of_persons = [Person(name='Taras', age=20, home=random.choice([True, False]), money=5000),
                       Person(name='Katya', age=25, home=random.choice([True, False]), money=7500),
                       Person(name='Dmytro', age=30, home=random.choice([True, False]), money=10000)]
    # 2. create houses.
    list_of_houses = [House(55, 45000), House(40, 30000), House(25, 25000), House(60, 55000)]
    # 3. create rieltor.
    rieltor = Rieltor('Leo', list_of_houses)
    # 4. Go to the job and make money.
    for person in list_of_persons:
        # 5. Check if person has house
        if person.home is False:
            person.working(25)
            for house in rieltor.list_houses:
                # 5.2 Check if person has enough money to buy house
                if person.home is False:
                    if person.money >= house.cost:
                        #6.buy house
                        person.buy_house()
                        print(rieltor.info_houses())
                        sell_house(rieltor=rieltor, person=person, house=house)
        else:
            print(f'{person.name} already has a house and don`t need to buy new.')
