class AiModel():
    def __init__(self):
        self.profile = 0
        self.min = 70
        self.max = 75

    def getProfile(self, profile_identification):
        self.profile = profile_identification
        self.min = Class().getMinimumPreferredTemperature(self.profile)
        self.max = Class().getMaximumPreferredTemperature(self.profile)

def main():
    model = AiModel()
    model.getProfile('001')
main()