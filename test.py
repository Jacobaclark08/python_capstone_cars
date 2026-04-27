class Vehicle:
    def __init__(self, brand, model, price, horsepower):
        self.brand = brand
        self.model = model
        self.price = price
        self.horsepower = horsepower

    def display_info(self):
        print(f"{self.brand} {self.model}: ${self.price:,}")

#cell 2
class SportsCar(Vehicle):
    def __init__(self, brand, model, price, horsepower, top_speed, zero_to_sixty):
        super().__init__(brand, model, price, horsepower)
        # Unique specs for sports cars
        self.top_speed = top_speed  # in mph
        self.zero_to_sixty = zero_to_sixty  # in seconds
        
    def calculate_value(self):
        if self.price > 0:
            return self.horsepower / self.price
        return 0

    def display_details(self):
        value = self.calculate_value()
        print(f"--- {self.brand} {self.model} Specs ---")
        print(f"Price: ${self.price:,}")
        print(f"Horsepower: {self.horsepower} hp")
        print(f"Top Speed: {self.top_speed} mph")
        print(f"0-60 mph: {self.zero_to_sixty}s")
        print(f"Value Ratio (HP/$): {value:.4f}")
        print("-" * 30)
        return value

#cell 3
car1 = SportsCar("Ford", "Mustang GT", 45000, 480, 160, 4.2)
car2 = SportsCar("Chevrolet", "Corvette ZR1X", 150000, 1000, 215, 1.7) #
car3 = SportsCar("Nissan", "Z", 43000, 400, 155, 4.5) #

cars= [car1, car2, car3]

#Cell 4

print("Sports Car Database\n")
best_value = 0
best_car = None

for car in cars:
    current_value = car.display_details()
    # Find the best value car
    if current_value > best_value:
        best_value = current_value
        best_car = car
#cell 5

print(f"Best Value for Money (Highest HP per Dollar):")
print(f"{best_car.brand} {best_car.model} at {best_value:.4f} HP/$")

#Cell 6

class Supercar(Vehicle):
    def __init__(self, brand, model, price, horsepower, top_speed, zero_to_sixty):
        super().__init__(brand, model, price, horsepower)
        # Unique specs for super cars
        self.top_speed = top_speed  # in mph
        self.zero_to_sixty = zero_to_sixty  # in seconds
        
    def calculate_value(self):
        if self.price > 0:
            return self.horsepower / self.price
        return 0

    def display_details(self):
        value = self.calculate_value()
        print(f"--- {self.brand} {self.model} Specs ---")
        print(f"Price: ${self.price:,}")
        print(f"Horsepower: {self.horsepower} hp")
        print(f"Top Speed: {self.top_speed} mph")
        print(f"0-60 mph: {self.zero_to_sixty}s")
        print(f"Value Ratio (HP/$): {value:.4f}")
        print("-" * 30)
        return value

#Cell 7 

car1 = SuperCar("Lamborghini", "Fenemo", 3500000, 1069, 217, 2.4)
car2 = SuperCar("Mclaren", "Speedtail", 3000000, 1035, 250, 2.3) 
car3 = SuperCar("Ferrari", "SF90 Stradale", 530000, 986, 211, 2.0) 

cars= [car1, car2, car3]
