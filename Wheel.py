import random

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
