from electrolyzer.optimization.solver import Solver
import casadi as ca


def run_simulation():
    # Create solver in 'optimization' mode
    solver = Solver(mode="simulation")
    # Build the NLP problem
    nlp = solver.build_nlp()
    # Create CasADi IPOPT solver
    opt = ca.nlpsol("opt", "ipopt", nlp)
    # Define variable bounds and initial guess
    n_vars = nlp["x"].size()[0]
    x0 = [1.0] * n_vars  # Initial guess
    lbx = [0.0] * n_vars  # Lower bounds
    ubx = [10.0] * n_vars  # Upper bounds

    n_constraints = nlp["g"].size()[0]
    lbg = [0.0] * n_constraints
    ubg = [0.0] * n_constraints
    p_val = [1.5, 60.0]
    # Solve the problem
    sol = opt(x0=x0, lbx=lbx, ubx=ubx, lbg=lbg, ubg=ubg, p=p_val)

    # Extract solution
    x_opt = sol["x"].full().flatten()
    print("Optimal decision variables:", x_opt)


if __name__ == "__main__":
    run_simulation()
