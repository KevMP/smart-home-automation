from class_model import Model

def establish_temperature_model():
    airconditioner_model = Model()
    airconditioner_model.addDecision("raise")
    airconditioner_model.addDecision("lower")
    airconditioner_model.addDecision("do_nothing")
    return airconditioner_model