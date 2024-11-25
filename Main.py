# Python script to create the wheel of fate
import os
from Wheel import Wheel
from Storage import (load_choces, save_choices, export_choices_to_csv, import_choices_from_csv)

CHOICES_FILE = 'choices.json'

def display_menu():
    # Display the main menu
    print("\n=== Wheel of Fate ===")
    print("1. View choices")
    print("2. Add a choice")
    print("3. Remove a choice")
    print("4. Spin the wheel")
    print("5. Export choices to CSV")
    print("6. Import choices from CSV")
    print("7. Exit")

def main():
    # Add Predefined chouces
    predefined_choices = []

    # Load custom choices
    custom_choices = load_choces(CHOICES_FILE)

    # Initialize the wheel
    wheel = Wheel(predefined_choices, custom_choices)

    while True:
        display_menu()
        choice = input("Enter choice: ")

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
                if 0 <= to_remove < len(wheel.custom_choices):
                    removed_choice = wheel.custom_choices[to_remove]
                    wheel.remove_choice(removed_choice)
                    print(F"{removed_choice} has been removed")
                else:
                    print("Invalid Selection!")
            except ValueError:
                print("Please enter a valid number")
        elif choice == "4": # Spin wheel
            result = wheel.spin_wheel(spins=15, delays=0.2)
            # print(f"/nThe Wheel of Fate says {result}")
        elif choice == "5": # Export choices to csv
            export_path = input("Enter file to export: ")
            export_choices_to_csv(export_path, wheel.all_choices)
            print(f"Choices exported to {export_path}")
        elif choice == "6": # Import choices from csv
            import_path = input("Enter path of imprt file: ")
            imported_choices = import_choices_from_csv(import_path)
            if imported_choices:
                for choice in imported_choices:
                    wheel.add_choice(choice)
                print(f"{len(imported_choices)} choices imported from file")
        elif choice == "7": # exit
            save_choices(CHOICES_FILE, wheel.custom_choices)
            print("Choices Saved! Goodbye!")
            break
        else:
            print("Invalid Option, please try again")

if __name__ == "__main__":
    main()
