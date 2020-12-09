import random


class Animal:
    home_planet = "Earth"

    # Constructor (makes instances of the class)
    def __init__(self,
                 num_legs,
                 num_arms,
                 color,
                 is_alive=True,
                 is_extinct=False,
                 is_mythical=False):
        self.num_legs = num_legs
        self.num_arms = num_arms
        self.color = color
        self.is_alive = is_alive
        self.total_limbs_val = num_arms + num_legs
        self.is_extinct = is_extinct
        self.is_mythical = is_mythical

    # Magic method to print for devs
    def __repr__(self):
        return "Animal({}, {}, '{}', {}, {}, {})" \
            .format(self.num_legs,
                    self.num_arms,
                    self.color,
                    self.is_alive,
                    self.is_mythical,
                    self.is_extinct)

    # Magic method to print for user
    def __str__(self):
        return "Number of Legs: {}\n" \
               "Number of Arms: {}\n" \
               "Color: {}\n" \
               "Alive: {}\n" \
               "Mythical: {}\n" \
               "Extinct: {}" \
            .format(self.num_legs,
                    self.num_arms,
                    self.color,
                    self.is_alive,
                    self.is_mythical,
                    self.is_extinct)

    # Overload '+' operator to create hybrid animal
    def __add__(self, other):
        if self.is_alive and other.is_alive:
            hybrid_num_legs = random.choice([self, other]).num_legs
            hybrid_num_arms = random.choice([self, other]).num_arms
            hybrid_color = random.choice([self, other]).color
            hybrid_is_extinct = self.is_extinct or other.is_extinct
            hybrid_is_mythical = self.is_mythical or other.is_mythical
            return Animal(hybrid_num_legs,
                          hybrid_num_arms,
                          hybrid_color,
                          True,
                          hybrid_is_extinct,
                          hybrid_is_mythical)
        else:
            print("One of these animals is dead!")

    # Alternate class constructor (makes instances of the class from strings)
    @classmethod
    def from_string(cls, string):
        (num_legs, num_arms, color,
         is_extinct, is_mythical) = string.split(" ")
        num_legs = int(num_legs)
        num_arms = int(num_arms)
        is_extinct = bool(is_extinct)
        is_mythical = bool(is_mythical)
        return cls(num_legs, num_arms, color, is_extinct, is_mythical)

    # Method to kill the animal
    def kill(self):
        self.is_alive = False

    # Method that calculates total limbs
    def total_limbs(self):
        return self.num_legs + self.num_arms

    # Class Method that sets home_planet Class Variable
    @classmethod
    def set_home_planet(cls, planet):
        cls.home_planet = planet

    # Static Method that prints a header
    @staticmethod
    def print_animals_header():
        print("----Animals Are Cool----")


horse = Animal(4, 0, "brown")
unicorn = Animal(4, 0, "white", is_mythical=True)
dog = Animal.from_string("4 0 black False False")

Animal.print_animals_header()

horse.kill()
hybrid = horse + unicorn
print(hybrid)
