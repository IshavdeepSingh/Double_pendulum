# -------  Importing Libraries ------- #

import numpy as np
from scipy.integrate import odeint
import sympy as sm

# -------  Defining Symbols & Variables ------- #

t = sm.symbols('t')
m_1, m_2, g = sm.symbols('m_1 m_2 g', positive=True)

the1, the2 = sm.symbols(r'\theta_1, \theta_2', cls=sm.Function) # sm.Function states that the position is a function

the1 = the1(t) # Specifying the variable
the2 = the2(t)

x1 = sm.sin(the1)
y1 = -sm.cos(the1)

x2 = x1 + sm.sin(the2)
y2 = y1 + -sm.cos(the2)

# -------  Defining Derivatives ------- #

the1_d = sm.diff(the1, t) # Angular Velocity
the1_dd = sm.diff(the1_d, t) # Angular Acceleration

x1_d = sm.diff(x1, t)
y1_d = sm.diff(y1, t)

the2_d = sm.diff(the2, t) # Angular Velocity
the2_dd = sm.diff(the2_d, t) # Angular Acceleration

x2_d = sm.diff(x2, t)
y2_d = sm.diff(y2, t)

# -------  Defining Energies & Lagrange ------- #

T_1 = 1/2 * m_1 * ((x1_d)**2+(y1_d)**2)
T_2 = 1/2 * m_2 * ((x2_d)**2+(y2_d)**2)
V_1 = m_1 * g * y1
V_2 = m_2 * g * y2
L = T_1 + T_2 - (V_2 + V_1)



# -------  Defining Lagrange's Equations ------- #

LE1 = sm.diff(sm.diff(L, the1_d), t) - sm.diff(L, the1) # use .simplyfy() if necessary
LE2 = sm.diff(sm.diff(L, the2_d), t) - sm.diff(L, the2) # use .simplyfy() if necessary

LE1 = LE1.simplify()
LE2 = LE2.simplify()


# -------  Solving the System of Equations & Lambdifying ------- #

solutions = sm.solve([LE1, LE2], the1_dd, the2_dd)
LEF1 = sm.lambdify((the1, the2, the1_d, the2_d, t, m_1, m_2, g), solutions[the1_dd])
LEF2 = sm.lambdify((the1, the2, the1_d, the2_d, t, m_1, m_2, g), solutions[the2_dd])

