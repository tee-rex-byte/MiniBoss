"""
Mini Boss Application

This application is designed to help you decide what project to work on next.
"""
from tkinter import Tk, Label, Button, Frame, TOP
import random as rn
from dictionaries import (
    machine_learning,
    games,
    data_science,
    numpy_projects,
    django_projects,
    flask_projects,
    nonsense,
    no_nonsense)


class MiniBoss:
    """Main class for the Mini Boss Application"""

    def __init__(self):
        self.root = Tk()
        self.root.title("Mini Boss")
        self.root.geometry("750x700")
        self.root.config(background="#637074")

        # Page Title
        self.title_label = Label(
            self.root,
            text="Mini Boss",
            bg="#637074",
            font=("Arial", 34, "bold"),
            fg="#f9f8f8"
        )
        self.title_label.pack(pady=5)

        self.subtitle_label = Label(
            self.root,
            text="Welcome to Mini Boss, can't decide what to do? Let me decide for you!",
            bg="#637074",
            font=("Arial", 15),
            fg="#f9f8f8"
        )
        self.subtitle_label.pack(pady=10)

        self.space_label = Label(
            self.root,
            text="",
            bg="#637074"
        )
        self.space_label.pack(pady=10)

        # Project Buttons

        # Displays Project
        self.result_label = Label(
            self.root,
            text="Click a button to see a random project",
            bg="#637074",
            font=("Arial", 14),
            fg="#ffffa7"
        )
        self.result_label.pack(pady=10)

        # Project Buttons
        self.button_to_category = {
            "Machine Learning": machine_learning,
            "Games": games,
            "Data Science": data_science,
            "Numpy": numpy_projects,
            "Django": django_projects,
            "Flask": flask_projects,
        }

        self.buttonframe = Frame(self.root, bg="#637074")
        self.buttonframe.pack(side=TOP, pady=20)

        button_names = list(self.button_to_category.keys())

        button_positions = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
        ]

        # 6 Buttons
        for i, name in enumerate(button_names):
            button = Button(
                self.buttonframe,
                text=name,
                command=lambda category=name: self.show_random_projects(category),
                bg="#aacfe4",
                width=20
            )
            button.grid(row=button_positions[i][0], column=button_positions[i][1], padx=10, pady=10)


        # Time Frame

        # Displays Time
        self.time_label = Label(
            self.root,
            text="Do you know how to do this?",
            bg="#637074",
            font=("Arial", 14),
            fg="#ffffa7"
        )
        self.time_label.pack(pady=10)

        # Time Buttons
        self.timeframe = Frame(self.root, bg="#637074")
        self.timeframe.pack(pady=20)

        time_positions = [(0,0), (0,1), (0,2)]

        self.time_to_category = {
            "I have NO idea": "30 days",
            "In the middle": "15 days",
            "Can do it with eyes closed": "3 days",
        }

        time_names = list(self.time_to_category.keys())

        for i, name in enumerate(time_names):
            button = Button(
                self.timeframe,
                text=name,
                command=lambda category=name: self.show_time(category),
                bg="#aacfe4",
                width=20
            )
            button.grid(row=time_positions[i][0], column=time_positions[i][1], padx=10, pady=10)


        # Words of encouragement

        # Displays Words of Encouragement
        self.encouragement_label = Label(
            self.root,
            text="Words of encouragement",
            bg="#637074",
            font=("Arial", 14),
            fg="#ffffa7"
        )
        self.encouragement_label.pack(pady=10)

        # Buttons of encouragement
        self.encouragement_frame = Frame(self.root, bg="#637074")
        self.encouragement_frame.pack(pady=20)

        words_positions = [(0,0), (0,1), (0,2)]
        self.encouragement_to_category = {
            "Expectation": nonsense,
            "Reality": no_nonsense
        }
        encouragement_names = list(self.encouragement_to_category.keys())

        for i, name in enumerate(encouragement_names):
            button = Button(
                self.encouragement_frame,
                text=name,
                command=lambda category=name: self.show_encouragement(category),
                bg="#aacfe4",
                width=20
            )
            button.grid(row=words_positions[i][0], column=words_positions[i][1], padx=10, pady=10)


        # Reset and quit
        self.options_frame = Frame(self.root, bg="#637074")
        self.options_frame.pack(pady=20)

        self.reset_button = Button(
            self.options_frame,
            text="Reset",
            command=self.reset,
            bg="#e67e22",
            width=10
        )
        self.reset_button.grid(row=0, column=0, padx=5, pady=5)

        self.quit_button = Button(
            self.options_frame,
            text="Quit",
            command=self.root.quit,
            bg="#c0392b",
            width=10
        )
        self.quit_button.grid(row=0, column=1, padx=5, pady=5)

        self.root.mainloop()

    def show_random_projects(self, category):
        """Displays a random project from the given category"""

        selected_category = self.button_to_category[category]
        random_project = rn.choice(list(selected_category.values()))
        self.result_label.config(text=f"{category} Project: {random_project}")

    def show_time(self, category):
        """Shows the amount of time given for the project"""

        selected_category = self.time_to_category[category]
        self.time_label.config(text=f"You have {selected_category} to complete the project")

    def show_encouragement(self, category):
        """Shows words of encouragement based on the category"""
        selected_category = self.encouragement_to_category[category]
        random_encouragement = rn.choice(list(selected_category.values()))
        self.encouragement_label.config(text=f"{category} words: {random_encouragement}")

    def reset(self):
        """Resets the labels to their default values"""
        self.result_label.config(text="Click a button to see a random project")
        self.time_label.config(text="Do you know how to do this?")
        self.encouragement_label.config(text="Words of encouragement")



MiniBoss()
