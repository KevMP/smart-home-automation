## simulation.py

from model import Model
from sensor import Sensor
from airconditioner import AirConditioner
from profiles import Profile
import tkinter as tk
from tkinter import font
import random

class Gui:
    def __init__(self, master, simulation_instance, model_instance, num_sensors):
        self.master = master
        self.master.title("Temperature Monitor")
        self.WINDOW_WIDTH = str(750)
        self.WINDOW_HEIGHT = str(850)
        self.master.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

        self.model = model_instance
        self.temperature_font = font.Font(family="Helvetica", size=20)
        self.simulation_instance = simulation_instance

        self.main_frame = tk.Frame(master)
        self.main_frame.pack(expand=True, fill='both')

        self.temperature_label = tk.Label(self.main_frame, text="Current Temperature: 0", font=self.temperature_font)
        self.temperature_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_controls_frame()
        self.create_sensor_frame(num_sensors)
        self.create_profile_dropdown()

        self.CYCLE_SPEED = 1 / 100
        self.update_temperature()

    def create_controls_frame(self):
        self.controls_frame = tk.Frame(self.main_frame)
        self.controls_frame.grid(row=1, column=0, pady=5)

        self.range_frame = tk.Frame(self.controls_frame, bg="white")
        self.range_frame.grid(row=0, column=0, pady=10, columnspan=3, sticky='n')

        self.range_label = tk.Label(self.range_frame, text="Preferred Temperature Range:", font=("Helvetica", 10), bg="white")
        self.range_label.grid(row=0, column=0, pady=5)

        self.range_data_label = tk.Label(self.range_frame, text="[72, 74]", font=("Helvetica", 10), bg="white")
        self.range_data_label.grid(row=1, column=0, pady=5)

        self.button_frame = tk.Frame(self.controls_frame)
        self.button_frame.grid(row=0, column=3, pady=10)

        self.up_button = tk.Button(self.button_frame, text="↑", command=self.increase_temperature_range)
        self.up_button.grid(row=0, column=0, pady=0, padx=5)

        self.down_button = tk.Button(self.button_frame, text="↓", command=self.decrease_temperature_range)
        self.down_button.grid(row=1, column=0, pady=0, padx=5)

    def create_sensor_frame(self, num_sensors):
        self.sensor_frame = tk.Frame(self.main_frame, borderwidth=2, relief="groove")
        self.sensor_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky='n')

        self.sensor_labels = [tk.Label(self.sensor_frame, text=f"Sensor {i + 1}: 0.00") for i in range(num_sensors)]
        for i, label in enumerate(self.sensor_labels):
            row = i // 2
            col = i % 2
            label.grid(row=row, column=col, pady=5)

        canvas_height = len(self.sensor_labels) * 60
        self.visualization_canvas = tk.Canvas(self.sensor_frame, width=400, height=canvas_height, bg="white")
        self.visualization_canvas.grid(row=0, column=2, rowspan=len(self.sensor_labels), padx=10)

    def create_profile_dropdown(self):
        profiles = ["Default", "Away", "Cat"]

        def on_profile_change(event):
            selected_profile = profile_var.get()
            self.simulation_instance.profile = self.profile_mapping[selected_profile]
            self.simulation_instance.lower_bound = self.simulation_instance.profile.getLowerBound() - 2
            self.simulation_instance.upper_bound = self.simulation_instance.profile.getUpperBound() + 2
            self.range_data_label.config(text="[{}, {}]".format(*self.simulation_instance.profile.getPreferredTemperature()))

        profile_var = tk.StringVar(self.main_frame)
        profile_var.set("Default")

        profile_dropdown = tk.OptionMenu(self.main_frame, profile_var, *profiles, command=on_profile_change)
        profile_dropdown.grid(row=3, column=0, columnspan=2, pady=10, sticky='n')

        self.profile_mapping = {
            "Default": Profile(min_preferred_temperature=70, max_preferred_temperature=75, identification="Default"),
            "Away": Profile(min_preferred_temperature=65, max_preferred_temperature=78, identification="Away"),
            "Cat": Profile(min_preferred_temperature=72, max_preferred_temperature=74, identification="Cat"),
        }

    def update_temperature(self):
        """
        Update the displayed temperature and sensor information on the GUI.
        This function is called periodically to reflect changes in the simulation environment.
        It calculates the average sensor temperature, updates GUI labels, and visualizes sensor data.
        """
        self.simulation_instance.updateSensors()
        sensor_temperatures = self.simulation_instance.getSensorTemperatures()
        average_sensor_temperature = sum(sensor_temperatures) / len(sensor_temperatures)
        self.simulation_instance.current_temperature = average_sensor_temperature
        self.temperature_label.config(text=f"Temperature: {average_sensor_temperature:.2f} F")

        for i, label in enumerate(self.sensor_labels):
            label.config(text=f"Sensor {i + 1}: {sensor_temperatures[i]:.2f} F")

        self.visualization_canvas.delete("all")
        ac_position = (50, 200)
        sorted_sensors = sorted(enumerate(self.simulation_instance.sensors),
                                key=lambda x: x[1].distance_from_temperature_source, reverse=True)

        for i, (index, sensor) in enumerate(sorted_sensors):
            distance_factor = i
            sensor_position = (350 - sensor.distance_from_temperature_source * 10, 50 + distance_factor * 60)
            line_color = self.get_line_color(sensor_temperatures[index])
            self.draw_line(ac_position, sensor_position, line_color)

        self.simulation_instance.incrementCycles()
        self.master.after(10, self.update_temperature)

    def draw_line(self, start, end, temperature_change):
        self.visualization_canvas.create_line(start, end, fill="black", width=2)
        ac_position = (50, 200)
        sensor_radius = 8
        index = int((end[1] - 50) / 60)
        temperature = self.simulation_instance.getSensorTemperatureByIndex(index)
        node_color = self.get_node_color(temperature)
        self.visualization_canvas.create_oval(end[0] - sensor_radius, end[1] - sensor_radius, end[0] + sensor_radius,
                                              end[1] + sensor_radius, outline=node_color, fill=node_color)

        sensor_label = self.get_sensor_label(end)
        self.visualization_canvas.create_text(end[0], end[1] - sensor_radius - 5, text=sensor_label, fill="black")

    def get_node_color(self, temperature):
        if temperature is not None:
            if temperature > 74:
                return "red"
            elif temperature < 72:
                return "blue"
            else:
                return "green"
        else:
            return "black"

    def get_sensor_label(self, position):
        index = (position[1] - 50) // 60
        return str(index + 1)

    def get_line_color(self, temperature):
        if temperature > 74:
            return "red"
        elif temperature < 72:
            return "blue"
        else:
            return "green"

    def run_simulation(self):
        """
        Run the simulation loop, where the AI model takes actions based on the current state of the simulation.
        The AI model's action influences the behavior of the temperature control system and the simulation environment.
        """
        action = self.model.getAction()
        self.simulation_instance.setCurrentTemperature(action)
        self.model.reward(self.simulation_instance.isAiGettingCloserToTarget())

        preferred_temperature_range = self.simulation_instance.profile.getPreferredTemperature()
        average_sensor_temperature = sum(self.simulation_instance.getSensorTemperatures()) / len(self.simulation_instance.sensors)

        if average_sensor_temperature < preferred_temperature_range[0]:
            self.simulation_instance.air_conditioner.lower_temperature()
        elif average_sensor_temperature > preferred_temperature_range[1]:
            self.simulation_instance.air_conditioner.raise_temperature()
        else:
            self.simulation_instance.air_conditioner.do_nothing_to_temperature()

        self.master.after(int(self.CYCLE_SPEED * 1000), self.run_simulation)

    def increase_temperature_range(self):
        self.simulation_instance.increasePreferredTemperature()
        self.range_data_label.config(text="[{}, {}]".format(*self.simulation_instance.profile.getPreferredTemperature()))

    def decrease_temperature_range(self):
        self.simulation_instance.decreasePreferredTemperature()
        self.range_data_label.config(text="[{}, {}]".format(*self.simulation_instance.profile.getPreferredTemperature()))

if __name__ == "__main__":
    """
    Initializes the simulation, model, and GUI for the temperature monitoring system. 
    The Simulation class is not imported here, as it is expected to be imported in the demo.py file where the program is launched.
    """
    root = tk.Tk()
    num_sensors = 9
    simulation_instance = Simulation(num_sensors=num_sensors)
    model_instance = Model()
    app = Gui(root, simulation_instance, model_instance, num_sensors)
    root.after(int(app.CYCLE_SPEED * 1000), app.run_simulation)
    root.mainloop()
