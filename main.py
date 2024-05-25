import constants


class Car:
    def __init__(self, model: str):
        self.model = model
        self.year = constants.YEAR
        self.cost = constants.COST


    def __str__(self) -> str:
        return f"Model: {self.model}, year: {self.year}, cost: {self.cost}"


    def decrease_cost_for_each_kilometer_of_trip(self, trip_distance: int | float) -> int:
        """Takes the trip distance.
        Upon its launch, the cost of the car is reduced by UAH 10 for every kilometer of travel"""
        km = 10
        reduced_cost = trip_distance * km
        self.cost -= reduced_cost
        return self.cost

    @property
    def what_car_is_this(self) -> str:
        if self.cost > 10_000_000:
            return constants.Value.ELITE
        elif self.cost < 2_000_000:
            return constants.Value.ECONOMY
        else:
            return constants.Value.MIDDLE


skoda = Car("Škoda Fabia")
skoda.decrease_cost_for_each_kilometer_of_trip(100)
print(skoda)
