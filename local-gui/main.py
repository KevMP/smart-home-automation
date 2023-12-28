import tkinter as tk
from tkinter import ttk
from class_network_client import Client

class SmartThermostatApp(tk.Tk):
    def __init__(self, client):
        super().__init__()

        self.title("Smart AI Thermostat")
        self.geometry("480x320")

        self.client = client
        self.profiles = self.fetch_profiles()  # Fetch profiles from the server

        self.profiles_listbox = tk.Listbox(self)
        for profile in self.profiles:
            self.profiles_listbox.insert(tk.END, profile)
        self.profiles_listbox.grid(row=0, column=0, pady=5)

        self.update_profiles_button = ttk.Button(self, text="Update Profiles", command=self.update_profiles)
        self.update_profiles_button.grid(row=1, column=0, pady=10)

    def fetch_profiles(self):
        return self.client.get_profiles()

    def update_profiles(self):
        self.profiles = self.fetch_profiles()
        self.profiles_listbox.delete(0, tk.END) 
        for profile in self.profiles:
            self.profiles_listbox.insert(tk.END, profile)

if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()
