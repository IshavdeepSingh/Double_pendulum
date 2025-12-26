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
