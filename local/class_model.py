from database_root import *
class Model(Database):
    def __init__(self):
        super().__init__()
        self.action_matrix = [0, 0, 0]
        self.decision_tree = []
    
    def addDecision(self, decision):
        self.decision_tree.append(decision)