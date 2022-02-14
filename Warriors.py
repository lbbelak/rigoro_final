
class Warrior:
    def __init__(self, name, maximum_health):
        self.name = name
        self.maximum_health = maximum_health
        self.health = maximum_health
        self.is_alive = True

    def set_health(self, number: int) -> None:
        self.health = number
        if self.health <= 0:
            self.is_alive = False

    def __add__(self, other):
        if self.is_alive and other.is_alive:
            new_child = Warrior((self.name + " " + other.name), self.maximum_health + other.maximum_health)
            return new_child

    def __str__(self) -> str:
        first = "Warrior(name="+'"'+self.name + '"' + ", maximum_health="+str(self.maximum_health) + ", is_alive="
        if self.is_alive:
            final = first + "True" + ")"
        else:
            final = first + "False" + ")"
        return final

    def __sub__(self, other) -> None:
        if self.is_alive and other.is_alive:
            self.set_health(self.health - 1)
            other.set_health(other.health - 1)
        return None


xena = Warrior(name="Xena",  maximum_health=1)
assert str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=True)'
conan = Warrior(name="Barbar Conan",  maximum_health=2)
assert True == xena.is_alive == conan.is_alive

child = xena + conan
assert child.is_alive == True
assert child.name == "Xena Barbar Conan"
assert child.maximum_health == 3

fight = xena - conan
assert fight is None
assert xena.is_alive == False
assert conan.is_alive == True
assert str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=False)'

child_2 = xena + conan
assert child_2 is None
