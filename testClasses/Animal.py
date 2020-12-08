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
