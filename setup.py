"""Setup configuration for Calorie Counter application."""

from setuptools import setup, find_packages

setup(
    name="calorie-counter",
    version="1.0.0",
    description="A Python application for tracking daily calorie intake",
    author="DevOps CA3 Project",
    packages=find_packages(),
    install_requires=[
        "flask>=3.0.0",
        "pytest>=8.0.0",
        "coverage>=7.2.7",
        "pylint>=3.2.3",
        "selenium>=4.15.0",
        "bandit>=1.7.5",
        "safety>=2.3.5",
        "requests>=2.31.0",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "calorie-counter=calorie_counter.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.12",
    ],
)