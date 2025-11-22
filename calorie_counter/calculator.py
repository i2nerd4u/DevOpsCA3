"""Module for tracking food and daily calorie intake."""
class CalorieCounter:
    """Class to track daily calorie intake."""
    def __init__(self):
        """Initialize with empty meal list."""
        self.meals = []

    def add_food(self, food, calories):
        """Add a meal with calories. Raise ValueError if calories is negative."""
        if calories < 0:
            raise ValueError("Calories cannot be negative")
        self.meals.append({"food": food, "calories": calories})

    def total_calories(self):
        """Return total calories for the day."""
        return sum(meal["calories"] for meal in self.meals)

    def list_meals(self):
        """Return a list of all meals"""
        return self.meals

    def reset_day(self):
        """Reset total calories for a new day."""
        self.meals = []
