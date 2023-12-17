from class_model import Model

def establish_temperature_model():
    temperature_model = Model()
    temperature_model.addDecision("raise")
    temperature_model.addDecision("lower")
    temperature_model.addDecision("do_nothing")
    return temperature_model