# Python script to create the wheel of fate
import os
from Wheel import Wheel
from Storage import load_choces, save_choices

CHOICES_FILE = 'choices.json'

def display_menu():
    # Display the main menu
    print("\n=== Wheel of Fate ===")
    print("1. View choices")
    print("2. Add a choice")
    print("3. Remove a choice")
    print("4. Spin the wheel")
    print("5. Exit")

def main():
    # Add Predefined chouces
    predefined_choices = ["PomoPlus Development", "LeetCode", "FEZ Development", "Python for LLM"]

    # Load custom choices
    custom_choices = load_choces(CHOICES_FILE)

    # Initialize the wheel
    wheel = Wheel(predefined_choices, custom_choices)

    while True:
        display_menu()
        choice = input("Enter choice:")

        if choice == "1": # View Choices
            print("\nChoices on the Wheel")
            for idx, option in enumerate(wheel.all_choices, 1):
                print(f"{idx}, {option}")
        elif choice == "2": # Add new choice
            new_choice = input("Enter a new choice: ")
            if new_choice:
                wheel.add_choice(new_choice)
                print(f"{new_choice} has been added!")
            else:
                print("Inalid input! No choice added!")
        elif choice == "3": # Remove a choice
            print("\nCustom Choices:")
            for idx, option in enumerate(wheel.custom_choices, 1):
                print(f"{idx}, {option}")
            
            try:
                to_remove = int(input("Enter number of choice to remove: ")) - 1
                
