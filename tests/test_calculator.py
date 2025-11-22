import pytest
from calorie_counter.calculator import CalorieCounter

def test_add_and_total():
    c = CalorieCounter()
    c.add_food("Apple", 100)
    c.add_food("Banana", 200)
    assert c.total_calories() == 300

def test_negative_calories():
    c = CalorieCounter()
    with pytest.raises(ValueError):
        c.add_food("Soda", -50)

def test_reset_day():
    c = CalorieCounter()
    c.add_food("Sandwich", 400)
    c.reset_day()
    assert c.total_calories() == 0
