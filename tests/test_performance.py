"""Performance tests for the application."""
import time
import pytest
from calorie_counter.calculator import CalorieCounter

def test_add_food_performance():
    """Test that adding food items is performant."""
    counter = CalorieCounter()
    start_time = time.time()
    
    # Add 1000 food items
    for i in range(1000):
        counter.add_food(f"Food{i}", 100)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Should complete within 1 second
    assert execution_time < 1.0
    assert counter.total_calories() == 100000

def test_total_calories_performance():
    """Test that calculating total calories is performant."""
    counter = CalorieCounter()
    
    # Add many items
    for i in range(10000):
        counter.add_food(f"Food{i}", 50)
    
    start_time = time.time()
    total = counter.total_calories()
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    # Should complete within 0.1 seconds
    assert execution_time < 0.1
    assert total == 500000