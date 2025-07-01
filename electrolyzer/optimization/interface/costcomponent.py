import casadi as ca


class CostComponent:
    def __init__(self):
        super().__init__()
        self.cost = {}

    def add_cost(self, cost_name: str, expression):
        """The function turns cost to a casadi.MX
        For example, if the cost_name is energy cost, then
        this function will add a term in the optimization formula"""
        self.cost[cost_name] = expression
