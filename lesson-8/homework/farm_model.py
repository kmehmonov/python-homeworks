class Animal:
    """
    Base class
    """

    def __init__(self, name: str, species: str, age: int, weight: float) -> None:
        """
        Initializes an Animal instance.

        Args:
            name (str): The name of the animal.
            species (str): The species of the animal.
            age (int): The age of the animal in years.
            weight (float): The weight of the animal in kilograms.
        """
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if weight <= 0:
            raise ValueError("Weight must be positive.")
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def eat(self, food: str) -> None:
        """
        Shows the animal eating.

        Args:
            food (str): The type of food the animal is eating.
        """
        if not food.strip():
            raise ValueError("Food cannot be empty.")
        print(f"{self.name} the {self.species} is eating {food}.")

    def sleep(self) -> None:
        """
        Shows the animal sleeping.
        """
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self) -> None:
        """
        Abstract method for making sounds.
        It will be implemented by child classes.
        """
        raise NotImplementedError("Subclasses must implement make_sound()")


class Cow(Animal):
    """
    Class representing a cow on the farm. Inherits from Animal.
    """

    def __init__(self, name: str, age: int, weight: float, milk_production: float) -> None:
        """
        Initializes a Cow instance.

        Args:
            name (str): The name of the cow.
            age (int): The age of the cow in years.
            weight (float): The weight of the cow in kilograms.
            milk_production (float): The amount of milk produced daily in liters.
        """
        super().__init__(name, "Cow", age, weight)
        if milk_production < 0:
            raise ValueError("Milk production cannot be negative.")
        self.milk_production = milk_production

    def produce_milk(self) -> None:
        """
        Prints the daily milk production of the cow.
        """
        print(f"{self.name} produces {self.milk_production} liters of milk per day.")

    def make_sound(self) -> None:
        """
        Shows the sound a cow makes.
        """
        print(f"{self.name} says 'Moo!'")


class Chicken(Animal):
    """
    Class representing a chicken on the farm. Inherits from Animal.
    """

    def __init__(self, name: str, age: int, weight: float, eggs_per_day: int) -> None:
        """
        Initializes a Chicken instance.

        Args:
            name (str): The name of the chicken.
            age (int): The age of the chicken in years.
            weight (float): The weight of the chicken in kilograms.
            eggs_per_day (int): The number of eggs laid daily.
        """
        super().__init__(name, "Chicken", age, weight)
        if eggs_per_day < 0:
            raise ValueError("Eggs per day cannot be negative.")
        self.eggs_per_day = eggs_per_day

    def lay_eggs(self) -> None:
        """
        Prints the number of eggs laid daily by the chicken.
        """
        print(f"{self.name} lays {self.eggs_per_day} eggs per day.")

    def make_sound(self) -> None:
        """
        Shows the sound a chicken makes.
        """
        print(f"{self.name} says 'Cluck!'")


class Pig(Animal):
    """
    Class representing a pig on the farm. Inherits from Animal.
    """

    def __init__(self, name: str, age: int, weight: float, mud_rolling: bool) -> None:
        """
        Initializes a Pig instance.

        Args:
            name (str): The name of the pig.
            age (int): The age of the pig in years.
            weight (float): The weight of the pig in kilograms.
            mud_rolling (bool): True if the pig is rolling in mud, False otherwise.
        """
        super().__init__(name, "Pig", age, weight)
        self.mud_rolling = mud_rolling

    def roll_in_mud(self) -> None:
        """
        Shows the pig rolling in mud.
        """
        if self.mud_rolling:
            print(f"{self.name} is happily rolling in the mud!")
        else:
            print(f"{self.name} is clean and not interested in mud.")

    def make_sound(self) -> None:
        """
        Shows the sound a pig makes.
        """
        print(f"{self.name} says 'Oink!'")


if __name__ == "__main__":

    # Create animals
    olaxon: Cow = Cow(name="Olaxon", age=5, weight=500.0, milk_production=20)
    chipchip: Chicken = Chicken(name="Chipchip", age=2, weight=3.0, eggs_per_day=5)
    baqaloq: Pig = Pig(name="Baqaloq", age=3, weight=150.0, mud_rolling=True)

    # Results
    olaxon.eat("grass")
    olaxon.produce_milk()
    olaxon.make_sound()

    chipchip.eat("corn")
    chipchip.lay_eggs()
    chipchip.make_sound()

    baqaloq.eat("scraps")
    baqaloq.roll_in_mud()
    baqaloq.make_sound()

