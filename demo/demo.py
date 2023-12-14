## demo.py

from model import Model
from simulation import Simulation
from gui import Gui
import tkinter as tk

def main():
    root = tk.Tk()
    simulation_instance = Simulation(num_sensors=9)
    gui = Gui(root, simulation_instance)
    root.after(int(gui.CYCLE_SPEED * 1000), gui.run_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()
