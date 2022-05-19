import enum


class User:
    def __init__(self, full_name, username, password, date_of_birth=None):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.full_name


class CarSize(enum.Enum):
    Sedan = 0,
    Hatchback = 1,
    Roadster = 2,
    CUV = 3,
    SUV = 4,
    Pickup = 5,
    Micro = 6,
    Cabriolet = 7,
    Supercar = 8,
    Coupe = 9,
    Van = 10


class Car:
    def __init__(self, car_name: str, size: CarSize, color=None, price_per_hour=0, mileage=0):
        self.car_name = car_name
        self.color = color
        self.price_per_hour = price_per_hour
        self.size = size
        self.mileage = mileage
        self.is_available = True
        self.customer = None

    def __str__(self):
        return self.size.name + ' ' + self.car_name

    def __repr__(self):
        return self.__str__()

    def get_price_per_day(self) -> int:
        return self.price_per_hour * 24

    def get_price_per_week(self) -> int:
        return self.get_price_per_day() * 7

    def get_price_per_month(self) -> int:
        return self.get_price_per_week() * 30

    def rent(self, customer: User):
        self.is_available = False
        self.customer = customer
        return self


class Dealer:
    def __init__(self, name, cars=None):
        if cars is None:
            cars = []

        self.name = name
        self.cars = cars

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def get_cars(self):
        return self.cars

    def get_cars_by_price(self, min_price=0, max_price=None):
        filtered_cars = []
        for car in self.cars:
            if max_price:
                if max_price > car.price_per_hour > min_price:
                    filtered_cars.append(car)
            elif car.price_per_hour >= min_price:
                filtered_cars.append(car)
        return filtered_cars

    def get_cars_by_size(self, size: CarSize):
        filtered_cars = []
        for car in self.cars:
            if car.size == size:
                filtered_cars.append(car)
        return filtered_cars

    def add_car(self, car: Car):
        self.cars.append(car)


if '__main__' == __name__:
    cars = ['Tesla', 'Mercedes', 'Audi', 'Citroen', 'Peugeot', 'Volkswagen', 'BMW']
    dealer = Dealer('Almaty Motors')
    for car_name in cars:
        dealer.add_car(Car(car_name, size=CarSize.Sedan, price_per_hour=10))
    dealer.add_car(Car('Dodge', CarSize.Pickup, price_per_hour=150))
    print(dealer.get_cars())
    print(dealer.get_cars_by_size(CarSize.Sedan))
    print(dealer.get_cars_by_price(max_price=100))
