import tkinter as tk
from tkinter import ttk
import sqlite3

class SmartThermostatApp(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("arc")

        self.title("Smart AI Thermostat")
        self.geometry("480x320")  

        self.current_temperature = tk.DoubleVar(value=72)
        self.temperature_unit = tk.StringVar(value="°F")
        self.thermostat_mode = tk.StringVar(value="Auto")

        self.notification_messages = ["Welcome", "AC Unit Running Smoothly", "Filter Needs Replacement"]
        self.current_message_index = 0

        
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        x_position = (window_width - 480) // 2
        y_position = (window_height - 320) // 2

        self.geometry(f"480x320+{x_position}+{y_position}")

        self.notification_label = ttk.Label(self, text="Notification message here", font=("Arial", 10))
        self.notification_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.temperature_label = ttk.Label(self, text=f"Temperature: {self.current_temperature.get():.1f}{self.temperature_unit.get()}", font=("Arial", 12))
        self.temperature_label.grid(row=1, column=0, columnspan=3, pady=5)

        self.mode_label = ttk.Label(self, text=f"Mode: {self.thermostat_mode.get()}", font=("Arial", 12))
        self.mode_label.grid(row=2, column=0, columnspan=3, pady=5)

        self.time_label = ttk.Label(self, text="", font=("Arial", 10))
        self.time_label.grid(row=3, column=0, columnspan=3, pady=5)

        self.slider = ttk.Scale(self, from_=20, to=95, orient="horizontal", length=180, variable=self.current_temperature, command=self.update_temperature, style="Temperature.Horizontal.TScale")
        self.slider.set(self.current_temperature.get())
        self.slider.grid(row=4, column=0, columnspan=3, pady=5)

        self.unit_toggle_button = ttk.Button(self, text="Toggle Unit", command=self.toggle_temperature_unit)
        self.unit_toggle_button.grid(row=5, column=0, pady=5)

        self.mode_toggle_button = ttk.Button(self, text="Toggle Mode", command=self.toggle_thermostat_mode)
        self.mode_toggle_button.grid(row=5, column=1, pady=5)

        self.create_profile_button = ttk.Button(self, text="Create Profile", command=self.show_profile_screen)
        self.create_profile_button.grid(row=5, column=2, pady=5)

        self.manage_profiles_button = ttk.Button(self, text="Manage Profiles", command=self.show_profile_screen)
        self.manage_profiles_button.grid(row=6, column=0, pady=5)

        self.show_vents_button = ttk.Button(self, text="Show Active Vents", command=self.show_active_vents)
        self.show_vents_button.grid(row=6, column=1, pady=5)

        self.house_label = None  # storing house label.

        self.notification_animation()
        self.update_time()
        self.profile_screen = None  

    def update_temperature(self, value):
        self.temperature_label.config(text=f"Temperature: {self.current_temperature.get():.1f}{self.temperature_unit.get()}")

    def toggle_temperature_unit(self):
        if self.temperature_unit.get() == "°F":
            self.temperature_unit.set("°C")
        else:
            self.temperature_unit.set("°F")
            self.update_temperature(None)
            
        if self.profile_screen and getattr(self.profile_screen, 'update_unit_label', None):
            self.profile_screen.update_unit_label()

    def toggle_thermostat_mode(self):
        modes = ["Auto", "Heat", "Cool"]
        current_mode = self.thermostat_mode.get()
        next_mode_index = (modes.index(current_mode) + 1) % len(modes)
        self.thermostat_mode.set(modes[next_mode_index])
        self.mode_label.config(text=f"Mode: {self.thermostat_mode.get()}")

    def notification_animation(self):
        self.notification_label.config(text=self.notification_messages[self.current_message_index])
        self.current_message_index = (self.current_message_index + 1) % len(self.notification_messages)
        self.after(2000, self.notification_animation)

    def show_profile_screen(self):
        self.profile_screen = ProfileScreen(self)
        self.profile_screen.grab_set()
        self.profile_screen.wait_window()

    def save_profile_to_db(self, profile_name, max_temp, min_temp, ac_mode, ai_sensitivity):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT, max_temp REAL, min_temp REAL, ac_mode TEXT, ai_sensitivity REAL)")
        cursor.execute("INSERT INTO profiles VALUES (?, ?, ?, ?, ?)", (profile_name, max_temp, min_temp, ac_mode, ai_sensitivity))
        connection.commit()
        connection.close()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.after(1000, self.update_time)

    def show_active_vents(self):
        vents_screen = VentsScreen(self)
        vents_screen.grab_set()
        vents_screen.wait_window()

        if self.house_label:
            self.house_label.destroy()

        self.create_house_diagram()

    def create_house_diagram(self):
        #house_image = Image.open('C:\\GitHub\\smart-home-automation\\local-gui\\Assets\\house.png')


        house_image = house_image.resize((200, 200))

        house_photo = ImageTk.PhotoImage(house_image)

        self.house_label = ttk.Label(self, image=house_photo)
        self.house_label.photo = house_photo
        self.house_label.grid(row=7, column=0, columnspan=3, pady=5)

        
        self.vents_status_label = ttk.Label(self, text="", font=("Arial", 10))
        self.vents_status_label.grid(row=8, column=0, columnspan=3, pady=5)

        
        self.slider_unit_label = ttk.Label(self, text=self.temperature_unit.get(), font=("Arial", 10))
        self.slider_unit_label.grid(row=9, column=0, columnspan=3, pady=5)

class ProfileScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Create Profile")
        self.geometry("400x300")

        self.master = master

        self.profile_name_label = ttk.Label(self, text="Profile Name:")
        self.profile_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.profile_name_entry = ttk.Entry(self)
        self.profile_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.max_temp_label = ttk.Label(self, text="Maximum Temperature:")
        self.max_temp_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.max_temp_var = tk.DoubleVar(value=72)
        self.max_temp_slider = ttk.Scale(self, from_=50, to=95, orient="horizontal", length=200, variable=self.max_temp_var, command=self.update_max_temp)
        self.max_temp_slider.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.max_temp_label_display = ttk.Label(self, text=f"Max Temp: {self.max_temp_var.get():.1f}°F")
        self.max_temp_label_display.grid(row=2, column=0, columnspan=2, pady=5)

        self.min_temp_label = ttk.Label(self, text="Minimum Temperature:")
        self.min_temp_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.min_temp_var = tk.DoubleVar(value=62)
        self.min_temp_slider = ttk.Scale(self, from_=50, to=95, orient="horizontal", length=200, variable=self.min_temp_var, command=self.update_min_temp)
        self.min_temp_slider.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.min_temp_label_display = ttk.Label(self, text=f"Min Temp: {self.min_temp_var.get():.1f}°F")
        self.min_temp_label_display.grid(row=4, column=0, columnspan=2, pady=5)

        self.ac_mode_label = ttk.Label(self, text="AC Mode:")
        self.ac_mode_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.ac_mode_combobox = ttk.Combobox(self, values=["Cool", "Heat", "Auto"])
        self.ac_mode_combobox.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        self.ac_mode_combobox.set("Cool")  # Default to Cool mode

        self.ai_sensitivity_label = ttk.Label(self, text="AI Sensitivity:")
        self.ai_sensitivity_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.ai_sensitivity_var = tk.DoubleVar(value=50)
        self.ai_sensitivity_scale = ttk.Scale(self, from_=0, to=100, orient="horizontal", length=200, variable=self.ai_sensitivity_var, command=self.update_ai_sensitivity)
        self.ai_sensitivity_scale.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        self.ai_sensitivity_label_display = ttk.Label(self, text=f"AI Sensitivity: {self.ai_sensitivity_var.get():.1f}")
        self.ai_sensitivity_label_display.grid(row=7, column=0, columnspan=2, pady=5)

        self.create_button = ttk.Button(self, text="Create Profile", command=self.create_profile)
        self.create_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=9, column=0, columnspan=2, pady=5)


    def update_unit_label(self):
        self.master.update_temperature(None)

    def update_max_temp(self, value):
        self.max_temp_label_display.config(text=f"Max Temp: {self.max_temp_var.get():.1f}°F")

    def update_min_temp(self, value):
        self.min_temp_label_display.config(text=f"Min Temp: {self.min_temp_var.get():.1f}°F")

    def update_ai_sensitivity(self, value):
        self.ai_sensitivity_label_display.config(text=f"AI Sensitivity: {self.ai_sensitivity_var.get():.1f}")

    def create_profile(self):
        profile_name = self.profile_name_entry.get()
        max_temp = self.max_temp_var.get()
        min_temp = self.min_temp_var.get()
        ac_mode = self.ac_mode_combobox.get()
        ai_sensitivity = self.ai_sensitivity_var.get()

    def save_profile_to_db(self, profile_name, max_temp, min_temp, ac_mode, ai_sensitivity):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT, max_temp REAL, min_temp REAL, ac_mode TEXT, ai_sensitivity REAL)")
        cursor.execute("INSERT INTO profiles VALUES (?, ?, ?, ?, ?)", (profile_name, max_temp, min_temp, ac_mode, ai_sensitivity))
        connection.commit()
        connection.close()

class VentsScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Manage Vents")
        self.geometry("300x200")

        self.master = master

        self.vents_status = {"Living Room": tk.BooleanVar(value=True), "Bedroom": tk.BooleanVar(value=False)}

        for vent, status in self.vents_status.items():
            vent_checkbox = ttk.Checkbutton(self, text=vent, variable=status)
            vent_checkbox.pack(pady=5)

        self.ok_button = ttk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=5)

if __name__ == '__main__':
    app = SmartThermostatApp()
    app.mainloop()