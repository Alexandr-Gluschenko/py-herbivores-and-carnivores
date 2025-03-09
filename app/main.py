class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        print(f"Herbivore is now {"hidden" if self.hidden else "visible"}")


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if isinstance(victim, Herbivore):
            if not victim.hidden:
                victim.health -= 50
                print(f"{self.name} bit {victim.name}"
                      f". {victim.name} now has {victim.health} health.")
            if victim.health <= 0:
                Animal.alive.remove(victim)
                print(f"{victim.name} has died.")
            else:
                print(f"{self.name} couldn't bite {victim.name}.")
