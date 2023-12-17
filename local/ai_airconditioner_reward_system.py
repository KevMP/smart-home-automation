import ai_airconditioner_model as ac_model

model = ac_model.establish_temperature_model()
print(model.action_matrix)
print(model.decision_tree)