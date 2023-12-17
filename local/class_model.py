class Model:
    def __init__(self):
        self.action_matrix = [0, 0, 0]
        self.decision_tree = []
    
    def addDecision(self, decision):
        self.decision_tree.append(decision)
    def getDecisionTree(self):
        return self.decision_tree