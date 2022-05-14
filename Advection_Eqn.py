# Finite difference methods to solve Riemann wave problems, from personal private CFD code repo


def lax_wendroff(u): 
    u[1:-1] = c/2.0*(1+c)*u[:-2] + (1-c**2)*u[1:-1] - c/2.0*(1-c)*u[2:]
    return u[1:-1]


# u denotes the flux variable

