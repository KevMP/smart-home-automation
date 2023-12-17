from ai_airconditioner_model import establish_temperature_model

model = establish_temperature_model()
print(model.action_matrix)
print(model.decision_tree)