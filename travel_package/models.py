"""Trip class (Object Oriented Programming)."""

from datetime import datetime

from .calculation import cost_per_day, cost_per_person


class Trip:
    def __init__(self, destination, days, travellers, travel, hotel, food,
                 misc=0.0, budget_limit=None, created=None):
        self.destination = destination
        self.days = days
        self.travellers = travellers
        self.travel = travel
        self.hotel = hotel
        self.food = food
        self.misc = misc
        self.budget_limit = budget_limit    # None means no limit
        self.created = created or datetime.now().strftime("%d-%m-%Y %H:%M")

    def total(self):
        return round(self.travel + self.hotel + self.food + self.misc, 2)

    def per_day(self):
        return round(cost_per_day(self.total(), self.days), 2)

    def per_person(self):
        return round(cost_per_person(self.total(), self.travellers), 2)

    def status(self):
        # tells if the trip is inside the budget limit
        if self.budget_limit is None:
            return "No budget limit set"
        difference = self.budget_limit - self.total()
        if difference >= 0:
            return f"Within budget (Rs. {difference:,.2f} left)"
        return f"Over budget (by Rs. {-difference:,.2f})"

    def to_dict(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
