# car_rental.py

import datetime

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_available_cars(self):
        print(f"Total cars available for rent: {self.stock}")
        return self.stock

    def rent_hourly(self, n):
        if n <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif n > self.stock:
            print(f"Sorry, only {self.stock} cars are available for rent.")
            return None
        else:
            self.stock -= n
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on hourly basis at {now.hour}:{now.minute}")
            return now

    def rent_daily(self, n):
        if n <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif n > self.stock:
            print(f"Sorry, only {self.stock} cars are available for rent.")
            return None
        else:
            self.stock -= n
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on daily basis at {now.hour}:{now.minute}")
            return now

    def rent_weekly(self, n):
        if n <= 0:
            print("Number of cars should be greater than zero.")
            return None
        elif n > self.stock:
            print(f"Sorry, only {self.stock} cars are available for rent.")
            return None
        else:
            self.stock -= n
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on weekly basis at {now.hour}:{now.minute}")
            return now

    def return_car(self, request):
        rental_time, rental_basis, num_of_cars = request
        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = datetime.datetime.now()
            rental_period = now - rental_time

            bill = 0
            if rental_basis == 1:  # hourly
                bill = rental_period.seconds / 3600 * 5 * num_of_cars
            elif rental_basis == 2:  # daily
                bill = rental_period.days * 20 * num_of_cars
            elif rental_basis == 3:  # weekly
                bill = (rental_period.days / 7) * 60 * num_of_cars

            print(f"Thanks for returning your car(s). Your bill is ${bill:.2f}")
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = None

    def request_car(self):
        cars = int(input("How many cars would you like to rent? "))
        if cars < 1:
            print("Number of cars should be greater than zero.")
            return -1
        else:
            self.cars = cars
            return self.cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0
