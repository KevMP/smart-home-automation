## demo.py

from simulation import Simulation
from gui import Gui
from model import Model
import tkinter as tk

def main():
    root = tk.Tk()
    num_sensors = 9
    simulation_instance = Simulation(num_sensors=num_sensors)
    model_instance = Model()
    gui = Gui(root, simulation_instance, model_instance, num_sensors)
    root.after(int(gui.CYCLE_SPEED * 1000), gui.run_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()
