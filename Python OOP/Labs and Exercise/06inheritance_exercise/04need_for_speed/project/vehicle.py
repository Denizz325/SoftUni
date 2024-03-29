class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometer: int) -> None:
        if self.fuel >= kilometer * self.fuel_consumption:
            self.fuel -= kilometer * self.fuel_consumption
