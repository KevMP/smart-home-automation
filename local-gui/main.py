import tkinter as tk
from tkinter import ttk, simpledialog
import sqlite3

class SmartThermostatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart AI Thermostat")
        self.geometry("400x300")

        self.current_temperature = 72
        self.notification_messages = ["Welcome", "AC Unit Running Smoothly", "Filter Needs Replacement"]
        self.current_message_index = 0

        self.notification_label = ttk.Label(self, text="Notification message here", font=("Arial", 12))
        self.notification_label.pack(pady=10)

        self.temperature_label = ttk.Label(self, text=f"Temperature: {self.current_temperature}°F", font=("Arial", 14))
        self.temperature_label.pack(pady=10)

        self.slider = ttk.Scale(self, from_=60, to=80, orient="horizontal", length=200, command=self.update_temperature)
        self.slider.set(self.current_temperature)
        self.slider.pack(pady=10)

        self.increase_button = ttk.Button(self, text="Increase Temperature", command=self.increase_temperature)
        self.increase_button.pack(pady=10)

        self.decrease_button = ttk.Button(self, text="Decrease Temperature", command=self.decrease_temperature)
        self.decrease_button.pack(pady=10)

        self.create_profile_button = ttk.Button(self, text="Create Profile", command=self.create_profile)
        self.create_profile_button.pack(pady=10)

        self.manage_profiles_button = ttk.Button(self, text="Manage Profiles", command=self.show_profile_screen)
        self.manage_profiles_button.pack(pady=10)

        self.notification_animation()

    def update_temperature(self, value):
        self.current_temperature = int(value)
        self.temperature_label.config(text=f"Temperature: {self.current_temperature}°F")

    def increase_temperature(self):
        self.current_temperature += 1
        self.slider.set(self.current_temperature)

    def decrease_temperature(self):
        self.current_temperature -= 1
        self.slider.set(self.current_temperature)

    def create_profile(self):
        profile_name = simpledialog.askstring("Create Profile", "Enter profile name:")
        if profile_name:
            self.save_profile_to_db(profile_name)
            print(f'Profile "{profile_name}" created with temperature {self.current_temperature}°F')

    def notification_animation(self):
        self.notification_label.config(text=self.notification_messages[self.current_message_index])
        self.current_message_index = (self.current_message_index + 1) % len(self.notification_messages)
        self.after(2000, self.notification_animation)

    def show_profile_screen(self):
        profile_screen = ProfileScreen(self)
        profile_screen.grab_set() 
        profile_screen.wait_window()

    def save_profile_to_db(self, profile_name):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT, temperature INTEGER)")
        cursor.execute("INSERT INTO profiles VALUES (?, ?)", (profile_name, self.current_temperature))
        connection.commit()
        connection.close()

class ProfileScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Manage Profiles")
        self.geometry("300x200")

        self.master = master

        self.profile_listbox = tk.Listbox(self)
        self.profile_listbox.pack(pady=10)

        self.load_profiles()

        self.delete_button = ttk.Button(self, text="Delete Profile", command=self.delete_profile)
        self.delete_button.pack(pady=10)

        self.ok_button = ttk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=10)

    def load_profiles(self):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT, temperature INTEGER)")
        cursor.execute("SELECT * FROM profiles")
        profiles = cursor.fetchall()
        connection.close()

        for profile in profiles:
            self.profile_listbox.insert(tk.END, profile[0])

    def delete_profile(self):
        selected_profile_index = self.profile_listbox.curselection()
        if selected_profile_index:
            selected_profile_name = self.profile_listbox.get(selected_profile_index)
            self.delete_profile_from_db(selected_profile_name)
            self.profile_listbox.delete(selected_profile_index)

    def delete_profile_from_db(self, profile_name):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM profiles WHERE name=?", (profile_name,))
        connection.commit()
        connection.close()

if __name__ == '__main__':
    app = SmartThermostatApp()
    app.mainloop()
