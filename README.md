# Double Pendulum Simulation (Lagrangian + Numerical Integration)

This project simulates the motion of a **double pendulum** using **Lagrangian mechanics** to derive the equations of motion and **numerical integration** to compute the time evolution. The result is an animated trajectory of two coupled pendulums, demonstrating nonlinear dynamics and sensitivity to initial conditions.

---

## What this project does

- Defines the **double pendulum geometry** using angular coordinates:
  - \(\theta_1(t)\): angle of the first pendulum
  - \(\theta_2(t)\): angle of the second pendulum
- Uses **SymPy** to:
  - build kinetic energy \(T\) and potential energy \(V\)
  - form the **Lagrangian** \(L = T - V\)
  - apply **Lagrange’s equations** to obtain \(\ddot{\theta}_1\) and \(\ddot{\theta}_2\)
- Converts the second-order system into a **first-order ODE system**
- Uses **SciPy `odeint`** to numerically solve the system over time
- Uses **Matplotlib animation** to visualize the double pendulum motion

---

## Physics model

### Coordinates
The pendulum bob positions are defined as:

- First mass:
  - \(x_1 = \sin(\theta_1)\)
  - \(y_1 = -\cos(\theta_1)\)

- Second mass:
  - \(x_2 = x_1 + \sin(\theta_2)\)
  - \(y_2 = y_1 - \cos(\theta_2)\)

### Energies
- Kinetic energy:
  - \(T_1 = \frac{1}{2} m_1 (\dot{x}_1^2 + \dot{y}_1^2)\)
  - \(T_2 = \frac{1}{2} m_2 (\dot{x}_2^2 + \dot{y}_2^2)\)

- Potential energy:
  - \(V_1 = m_1 g y_1\)
  - \(V_2 = m_2 g y_2\)

- Lagrangian:
  - \(L = (T_1 + T_2) - (V_1 + V_2)\)

### Equations of motion
Lagrange’s equations are applied:

\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}_i}\right) - \frac{\partial L}{\partial \theta_i} = 0
\quad \text{for } i = 1,2
\]

SymPy solves these equations for \(\ddot{\theta}_1\) and \(\ddot{\theta}_2\). The resulting expressions are then converted into fast numerical functions using `lambdify`.

---

## Numerical method

The solver integrates a **first-order** system in the state vector:

\[
y = [\theta_1, \dot{\theta}_1, \theta_2, \dot{\theta}_2]
\]

The system returns:

\[
\frac{dy}{dt} = [\dot{\theta}_1, \ddot{\theta}_1, \dot{\theta}_2, \ddot{\theta}_2]
\]

Integration is performed using:

- **SciPy**: `scipy.integrate.odeint`
- Time grid:
  - `time_points = np.linspace(0, 40, 1001)`

---

## Requirements

Install dependencies:

```bash
pip install numpy scipy sympy matplotlib
