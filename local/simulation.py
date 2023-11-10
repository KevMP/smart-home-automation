from database import Database

class AiModel():
    def __init__(self):
        self.profile = 0
        self.min = 70
        self.max = 75

    def setProfile(self, profile_identification):
        self.profile = profile_identification
        self.min = Database().getMinimumPreferredTemperature(self.profile)
        self.max = Database().getMaximumPreferredTemperature(self.profile)

if __name__ == "__main__":
    model = AiModel()
    model.setProfile(0)
    print(model.min)