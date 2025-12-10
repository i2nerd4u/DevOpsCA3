"""Security tests for the application."""
import pytest
import requests
from calorie_counter.calculator import CalorieCounter

def test_input_validation():
    """Test that negative calories are rejected."""
    counter = CalorieCounter()
    with pytest.raises(ValueError):
        counter.add_food("Test", -100)

def test_sql_injection_protection():
    """Test basic SQL injection protection."""
    counter = CalorieCounter()
    # Should not raise exception with SQL-like input
    counter.add_food("'; DROP TABLE users; --", 100)
    assert len(counter.list_meals()) == 1

def test_xss_protection():
    """Test XSS protection in food names."""
    counter = CalorieCounter()
    xss_payload = "<script>alert('xss')</script>"
    counter.add_food(xss_payload, 100)
    meals = counter.list_meals()
    assert meals[0]['food'] == xss_payload  # Should store as-is, template will escape