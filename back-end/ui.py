# User Interface Application
class UserInterfaceApplication:
    def __init__(self, smart_thermostat, ai_agent):
        self.smart_thermostat = smart_thermostat
        self.ai_agent = ai_agent

    def view_settings(self):
        return self.smart_thermostat.get_status()

    def update_temperature_setting(self, new_temperature):
        self.smart_thermostat.set_temperature(new_temperature)
        return f"Temperature setting updated to {new_temperature}°C"

    def request_recommendation(self):
        current_state = (self.smart_thermostat.temperature_setting, self.smart_thermostat.ac_status)
        recommended_action = self.ai_agent.choose_action(current_state)
        return f"AI recommendation: {recommended_action}"

# Analytics Dashboard
class AnalyticsDashboard:
    def __init__(self):
        self.temperature_history = []
        self.humidity_history = []
        self.ac_status_history = []

    def update_data(self, temperature, humidity, ac_status):
        self.temperature_history.append(temperature)
        self.humidity_history.append(humidity)
        self.ac_status_history.append(ac_status)

    def get_summary(self):
        return {
            "Temperature": self.temperature_history,
            "Humidity": self.humidity_history,
            "AC Status": self.ac_status_history,
        }
