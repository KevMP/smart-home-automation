from database_root import *

"""
**********************************************************************************
The action matrix is where the ai(controller) will be getting the final output from, our decision
tree is responsible for controlling the actions in our matrix.

The decision tree's items would have to be declared on use, example,
    AI_CONTROLLER_FOR_LIGHTBULBS = Model()
    AI_CONTROLLER_FOR_LIGHTBULBS.addDecision('turn_off_lights')
    AI_CONTROLLER_FOR_LIGHTBULBS.addDecision('turn_on_lights')
**********************************************************************************
"""

class Model(Database):
    def __init__(self):
        super().__init__()
        self.action_matrix = ['output_something', 'output_something', 'output_something']
        self.decision_tree = []
    
    def addDecision(self, decision):
        self.decision_tree.append(decision)