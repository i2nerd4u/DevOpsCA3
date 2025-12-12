"""
Calorie Counter Package

A Python package for tracking daily calorie intake with CLI and web interfaces.
Supports adding meals, viewing totals, and resetting daily counts.
"""

__version__ = "1.0.0"
__author__ = "DevOps CA3 Project"

from .calculator import CalorieCounter

__all__ = ["CalorieCounter"]