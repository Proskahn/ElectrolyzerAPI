import casadi as ca


class StateComponent:
    def __init__(self):
        super().__init__()
        self.state: dict = {}

    def add_state(self, state_name: str):
        """The function turns state to a casadi.MX
        For example, if the state_name is current state, then"
        this function will add a term in the optimization formula"""
        self.state[state_name] = ca.MX.sym(state_name)
