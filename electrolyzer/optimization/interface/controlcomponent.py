import casadi as ca


class ControlComponent:
    def __init__(self):
        super().__init__()
        self.control = {}

    def add_control(self, control_name: str, value: float = 0):
        """The function turns control to a casadi.MX
        For example, if the control_name is water temperature, then
        this function will add a term in the optimization formula"""
        self.control[control_name] = ca.MX.sym(control_name)
