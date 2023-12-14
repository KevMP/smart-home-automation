## demo.py

from simulation import Simulation
from gui import Gui
from model import Model  # Import your AI class (replace 'AI' with the actual name)
import tkinter as tk

def main():
    root = tk.Tk()
    num_sensors = 9  # Change this to the desired number of sensors
    simulation_instance = Simulation(num_sensors=num_sensors)
    model_instance = Model()  # Create an instance of your Model class
    gui = Gui(root, simulation_instance, model_instance, num_sensors)  # Pass the AI instance and num_sensors
    root.after(int(gui.CYCLE_SPEED * 1000), gui.run_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()