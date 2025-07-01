class ConstraintComponent:
    """This component turn the name and equation of
    the constraint to Casadi Contraint"""

    def __init__(self):
        super().__init__()
        self.constraint = {}

    def add_constraint(self, constraint_name: str, constraint_expression):
        """This function pass the constraint name and expression
        to casadi contraint"""
        self.constraint[constraint_name] = constraint_expression
