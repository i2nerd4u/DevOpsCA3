"""CLI application for entering food items and tracking daily calories."""
from calorie_counter.calculator import CalorieCounter

if __name__ == "__main__":
    counter = CalorieCounter()
    while True:
        choice = input("1. Add food  2. View total  3. Reset  4. Exit: ")
        if choice == "1":
            food = input("Enter food name: ")
            cal = int(input("Enter calories: "))
            counter.add_food(food, cal)
        elif choice == "2":
            print("\nMeals Today:")
            for meals in counter.list_meals():
                print(f"- {meals['food']}: {meals['calories']} calories")
            print(f"Total calories: {counter.total_calories()}")
        elif choice == "3":
            counter.reset_day()
            print("Day reset.")
        elif choice == "4":
            print("Exiting application, goodbye!")
            break
