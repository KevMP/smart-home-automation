## Features of the file
## Display:
## Current temperature,
## IF the AC is ON/OFF.

## Functions:
## Manually being able to
## control the temperature.
import tkinter as tk
import os
from database import DATABASE

def main():
    applicationView = tk.Tk()
    applicationView.geometry("720*720")
    applicationView.update()

    current_time = DATABASE().getCurrentTime()
    temperature = DATABASE().getTemperature(current_time)
    airconditioner_status = DATABASE().getAirconditionerStatus()

    applicationView.mainloop()