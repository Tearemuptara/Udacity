from testClasses.Animal import Animal


class Insect(Animal):

    def __init__(self,
                 color,
                 is_alive=True):
        super().__init__(6, 0, color, is_alive, False, False)

    def __repr__(self):
        return "Insect({}, {}, '{}', {}, {}, {})" \
            .format(self.num_legs,
                    self.num_arms,
                    self.color,
                    self.is_alive,
                    self.is_mythical,
                    self.is_extinct)


dung_beetle = Insect("black")
print(dung_beetle)

print(dung_beetle.color)
print(dung_beetle.num_legs)

print(dung_beetle.is_alive)
dung_beetle.kill()
print(dung_beetle.is_alive)
