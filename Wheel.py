import random
import time
import sys

class Wheel:
    def __init__(self, predefined_choices, custom_choices):

        # Initialising wheel with predefined and custom choices
        self.predefined_choices = predefined_choices
        self.custom_choices = custom_choices

    @property
    def all_choices(self):
        # Combine all choices
        return self.predefined_choices + self.custom_choices
    
    def add_choice(self, choice):
        # Add new custom choices
        if choice not in self.custom_choices:
            self.custom_choices.append(choice)
    
    def remove_choice(self, choice):
        # Remove a custom choice
        if choice in self.custom_choices:
            self.custom_choices.remove(choice)
    
    def spin(self):
        if not self.all_choices:
            return "No choices available!"
        else:
            return random.choice(self.all_choices)
    
    def spin_wheel(self, spins=10, delays=0.1):
        # Spin the wheel with an animation effect
        # Consider empty wheel cases
        if not self.all_choices:
            return "No Choices Available!"
        
        for _ in range(spins):
            result = random.choice(self.all_choices)
            sys.stdout.write(f"\r🎉 {result}")
            sys.stdout.flush()
            return result
