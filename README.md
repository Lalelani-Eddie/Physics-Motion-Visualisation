# Spacecraft Motion Simulation (Web VPython)

**Author:** LALELANI EDDIE NENE  
**Student Number:** NNXLAL001  
**Platform:** Web VPython (GlowScript 3.2) / Python `vpython`  

---

## 🚀 Overview

This project simulates the coupled translational and rotational dynamics of a rigid spacecraft operating in a two-dimensional planar vacuum environment under an off-center (asymmetric) thrust force.

The simulation demonstrates fundamental principles of classical mechanics and computational physics, specifically illustrating how an applied thrust produces both linear acceleration at the center of mass (CM) and angular acceleration about the principal rotational axis.

---

## 🌌 Physical & Mathematical Formulation

### 1. Mass & Moment of Inertia
The spacecraft is modeled as a cylindrical/disk rigid body with:
- **Mass ($M$):** $3.2\text{ kg}$
- **Radius ($R$):** $0.87\text{ m}$
- **Inertia Geometric Factor ($c$):** $0.7$
- **Moment of Inertia ($I$):**
  $$I = c \cdot M \cdot R^2$$

### 2. Rotational Dynamics
The thrust force $\vec{F}$ is applied tangentially at a distance $R$ from the center of mass:
- **Torque ($\tau_z$):**
  $$\tau_z = (\vec{r}_{\text{rel}} \times \vec{F})_z = R \cdot F_{\text{thrust}}$$
- **Angular Acceleration ($\alpha$):**
  $$\alpha = \frac{\tau_z}{I}$$
- **Angular Velocity & Orientation Update (Euler-Cromer):**
  $$\omega(t + \Delta t) = \omega(t) + \alpha \Delta t$$
  $$\theta(t + \Delta t) = \theta(t) + \omega(t + \Delta t) \Delta t$$

### 3. Translational Dynamics
The center of mass accelerates according to Newton's Second Law:
- **Thrust Force Vector ($\vec{F}$):**
  $$\vec{F} = \begin{bmatrix} -F_{\text{thrust}} \sin(\theta) \\ F_{\text{thrust}} \cos(\theta) \\ 0 \end{bmatrix}$$
- **Linear Momentum Update:**
  $$\vec{p}_{\text{cm}}(t + \Delta t) = \vec{p}_{\text{cm}}(t) + \vec{F} \Delta t$$
- **Center of Mass Position Update:**
  $$\vec{r}_{\text{cm}}(t + \Delta t) = \vec{r}_{\text{cm}}(t) + \frac{\vec{p}_{\text{cm}}(t + \Delta t)}{M} \Delta t$$

---

## 🛠️ Simulation Parameters

| Parameter | Symbol | Value | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| Spacecraft Mass | $M$ | $3.2$ | $\text{kg}$ | Total body mass |
| Spacecraft Radius | $R$ | $0.87$ | $\text{m}$ | Characteristic radius of the body |
| Inertia Constant | $c$ | $0.7$ | — | Shape-dependent mass distribution factor |
| Thrust Magnitude | $F_{\text{thrust}}$ | $3.4$ | $\text{N}$ | Applied continuous thrust force |
| Initial Angle | $\theta_0$ | $-\pi / 2$ | $\text{rad}$ | Initial angular orientation |
| Time Step | $\Delta t$ | $0.005$ | $\text{s}$ | Numerical integration step size |
| Duration | $t_{\text{max}}$ | $10.0$ | $\text{s}$ | Total simulated time |

---

## 🎨 Visual Features

- **Spacecraft Body:** Rendered as a cyan translucent cylinder representing the physical extent of the vessel.
- **Thrust Point:** Highlighted with a green sphere locked to the edge of the spacecraft at angle $\theta$.
- **Center of Mass Trail (Yellow):** Traces the continuous path of $\vec{r}_{\text{cm}}(t)$.
- **Thrust Point Trail (Green):** Visualizes the cycloidal/spiral trajectory of the thruster point in space.

---

## 💻 How to Run

### Option A: GlowScript / Web VPython (Browser)
1. Open [Web VPython](https://www.glowscript.org/) or [Trinket.io](https://trinket.io/glowscript).
2. Create a new program with language set to **Web VPython 3.2**.
3. Paste the code and click **Run**.

### Option B: Local Python Environment
1. Install the `vpython` package:
   ```bash
   pip install vpython
