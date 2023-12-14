## gui.py

import tkinter as tk
from tkinter import font
from model import Model
from simulation import Profile

class Gui:
    def __init__(self, master, simulation_instance):
        self.master = master
        self.master.title("Temperature Monitor")
        self.WINDOW_WIDTH = str(300)
        self.WINDOW_HEIGHT = str(400)
        self.master.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")  # Increased height to accommodate the dropdown menu

        # Set a larger font for the temperature label
        self.temperature_font = font.Font(family="Helvetica", size=20)

        self.ai = Model()  # Use the imported Model class
        self.environment = simulation_instance  # Use the provided simulation_instance

        self.temperature_label = tk.Label(master, text="Current Temperature: 0", font=self.temperature_font)
        self.temperature_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_controls_frame()  # Create a frame for controls
        self.create_profile_dropdown()  # Create the profile dropdown menu

        # Frame for sensor labels
        self.sensor_frame = tk.Frame(master, borderwidth=2, relief="groove")
        self.sensor_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        # Labels to display individual sensor temperatures
        self.sensor_labels = [tk.Label(self.sensor_frame, text=f"Sensor {i+1}: 0.00") for i in range(len(self.environment.sensors))]
        for i, label in enumerate(self.sensor_labels):
            # Arrange sensors in pairs, stacked vertically
            row = i // 2
            col = i % 2
            label.grid(row=row, column=col, pady=5)

        self.CYCLE_SPEED = 1 / 100

        self.update_temperature()

    def create_controls_frame(self):
        # Frame for controls
        self.controls_frame = tk.Frame(self.master)
        self.controls_frame.grid(row=1, column=0, pady=5)

        # Frame for preferred temperature range
        self.range_frame = tk.Frame(self.controls_frame, bg="white")  # Set the background color to white
        self.range_frame.grid(row=0, column=0, pady=10)

        # Label to display preferred temperature range
        self.range_label = tk.Label(self.range_frame, text="Preferred Temperature Range:", font=("Helvetica", 10), bg="white")
        self.range_label.grid(row=0, column=0, pady=5)

        # Display the temperature range in a Label with a white background
        self.range_data_label = tk.Label(self.range_frame, text="[72, 74]", font=("Helvetica", 10), bg="white")
        self.range_data_label.grid(row=1, column=0, pady=5)

        # Frame for temperature buttons
        self.button_frame = tk.Frame(self.controls_frame)
        self.button_frame.grid(row=0, column=1, pady=10)

        # Up arrow button
        self.up_button = tk.Button(self.button_frame, text="↑", command=self.increase_temperature_range)
        self.up_button.grid(row=0, column=0, pady=0, padx=5)  # Set pady to 0

        # Down arrow button
        self.down_button = tk.Button(self.button_frame, text="↓", command=self.decrease_temperature_range)
        self.down_button.grid(row=1, column=0, pady=0, padx=5)  # Set pady to 0

    def create_profile_dropdown(self):
        profiles = ["Default", "Away", "Cat"]  # Add more profiles as needed

        def on_profile_change(event):
            selected_profile = profile_var.get()
            # Update the current profile and preferred temperature range
            self.environment.profile = self.profile_mapping[selected_profile]
            self.environment.lower_bound = self.environment.profile.getLowerBound() - 2
            self.environment.upper_bound = self.environment.profile.getUpperBound() + 2

            # Update the displayed temperature range
            self.range_data_label.config(text="[{}, {}]".format(*self.environment.profile.getPreferredTemperature()))

        # Dropdown menu
        profile_var = tk.StringVar(self.master)
        profile_var.set("Default")  # Default profile

        profile_dropdown = tk.OptionMenu(self.master, profile_var, *profiles, command=on_profile_change)
        profile_dropdown.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a mapping between profile names and Profile instances
        self.profile_mapping = {
            "Default": Profile(min_preferred_temperature=70, max_preferred_temperature=75, identification="Default"),
            "Away": Profile(min_preferred_temperature=65, max_preferred_temperature=78, identification="Away"),
            "Cat": Profile(min_preferred_temperature=72, max_preferred_temperature=74, identification="Cat"),
            # Add more profiles as needed
        }

    def update_temperature(self):
        self.environment.updateSensors()

        # Calculate the average sensor temperature
        sensor_temperatures = self.environment.getSensorTemperatures()
        average_sensor_temperature = sum(sensor_temperatures) / len(sensor_temperatures)

        # Update the current temperature
        self.environment.current_temperature = average_sensor_temperature
        self.temperature_label.config(text=f"Temperature: {average_sensor_temperature:.2f} F")

        # Update individual sensor labels
        for i, label in enumerate(self.sensor_labels):
            label.config(text=f"Sensor {i + 1}: {sensor_temperatures[i]:.2f} F")

        self.environment.incrementCycles()
        self.master.after(10, self.update_temperature)

    def run_simulation(self):
        action = self.ai.getAction()
        self.environment.setCurrentTemperature(action)
        self.ai.reward(self.environment.isAiGettingCloserToTarget())

        # Update air conditioner status based on the selected profile
        preferred_temperature_range = self.environment.profile.getPreferredTemperature()
        average_sensor_temperature = sum(self.environment.getSensorTemperatures()) / len(self.environment.sensors)

        if average_sensor_temperature < preferred_temperature_range[0]:
            self.environment.air_conditioner.lower_temperature()
        elif average_sensor_temperature > preferred_temperature_range[1]:
            self.environment.air_conditioner.raise_temperature()
        else:
            self.environment.air_conditioner.do_nothing_to_temperature()

        self.master.after(int(self.CYCLE_SPEED * 1000), self.run_simulation)

    def increase_temperature_range(self):
        self.environment.increasePreferredTemperature()
        self.range_data_label.config(text="[{}, {}]".format(*self.environment.profile.getPreferredTemperature()))

    def decrease_temperature_range(self):
        self.environment.decreasePreferredTemperature()
        self.range_data_label.config(text="[{}, {}]".format(*self.environment.profile.getPreferredTemperature()))
