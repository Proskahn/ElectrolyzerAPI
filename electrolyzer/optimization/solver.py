from electrolyzer.optimization.Electrolyzer import ElectrolyzerDigitalTwin
import casadi as ca


class Solver(ElectrolyzerDigitalTwin):
    "Solve the optimization problem"

    def __init__(self, mode="simulation"):
        """
        Initialize the solver.
        :param mode: str, either 'simulation' or 'optimization'
        """
        super().__init__()
        if mode not in ["simulation", "optimization"]:
            raise ValueError(
                f"Invalid mode: {mode}. Choose 'simulation' or 'optimization'"
            )
        self.mode = mode

    def all_costs(self):
        return ca.vertcat(*self.cost.values())

    def build_nlp(self):
        """
        Return CasADi dict for NLP solver.
        - In 'optimization' mode, both state and control are decision variables.
        - In 'simulation' mode, control is fixed, and only state is optimized.
        """
        # Initialize problem structure
        self.set_state()
        self.set_control()
        self.set_cost()
        self.set_constraint()

        if self.mode == "optimization":
            x = ca.vertcat(*self.state.values(), *self.control.values())
            g = ca.vertcat(*self.constraint.values())
            f = self.all_costs()
            p = ca.MX()
        elif self.mode == "simulation":
            # Here the control should be a given value
            # Where can I specify it?
            x = ca.vertcat(*self.state.values())
            p = ca.vertcat(*self.control.values())
            g = ca.vertcat(*self.constraint.values())
            f = ca.MX(0)  # No cost function in simulation mode

        return {"x": x, "p": p, "f": f, "g": g}


solver = Solver(mode="optimization")
nlp = solver.build_nlp()
