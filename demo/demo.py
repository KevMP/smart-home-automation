# demo.py
from model import Model
from simulation import Simulation
from gui import App
import tkinter as tk

def main():
    root = tk.Tk()
    simulation_instance = Simulation(num_sensors=9)
    app = App(root, simulation_instance)
    root.after(int(app.CYCLE_SPEED * 1000), app.run_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()
