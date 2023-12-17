from class_model import Model

if __name__ == "__main__":
    temperature_model = Model()
    temperature_model.addDecision("raise")
    temperature_model.addDecision("lower")
    temperature_model.addDecision("do_nothing")
    print(temperature_model.getDecisionTree())