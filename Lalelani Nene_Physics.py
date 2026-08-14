from vpython import *
#Web VPython 3.2
# PROGRAM TO DEMONSTRATE THE MOTION OF A SPACECRAFT
# LALELANI EDDIE NENE
# STUDENT NUMBER : NNXLAL001

from vpython import *

# CONSTANTS & PARAMETERS
M = 3.2
c = 0.7
R = 0.87
I = c * M * R**2

# INITIAL CONDITIONS
theta = -pi / 2.0         # Orientation angle (scalar in radians)
omega = 0.0               # Angular velocity around z-axis (scalar)
rcm = vector(0, 0, 0)     # Center-of-mass position
pcm = vector(0, 0, 0)     # Linear momentum
F_thrust = 3.4            # Thrust force magnitude

# VISUAL OBJECTS
# Spacecraft body represented at center of mass
spacecraft = cylinder(pos=rcm - vector(0, 0, 0.05), axis=vector(0, 0, 0.1), radius=R, color=color.cyan, opacity=0.5)

# Visual marker for thrust point and path trails
thrust_pos = rcm + vector(R * cos(theta), R * sin(theta), 0)
thrustpoint = sphere(pos=thrust_pos, radius=0.06, color=color.green)
trail_cm = curve(pos=[rcm], color=color.yellow, radius=0.02)
trail_thrust = curve(pos=[thrust_pos], color=color.green, radius=0.01)

# SIMULATION PARAMETERS
dt = 0.005
t = 0.0

# ANIMATION LOOP
while t < 10.0:
    rate(200)  # rate(1/dt) for real-time speed

    # 1. Geometry of the thrust point relative to center of mass
    r_rel = vector(R * cos(theta), R * sin(theta), 0)
    
    # 2. Force vector (assuming thrust is directed tangentially/perpendicular to radius vector)
    # Torque tau_z = (r x F)_z = R * F_thrust
    tau_z = R * F_thrust
    Fvector = vector(-F_thrust * sin(theta), F_thrust * cos(theta), 0)

    # 3. Rotational updates (Euler-Cromer)
    alpha = tau_z / I
    omega = omega + alpha * dt
    theta = theta + omega * dt

    # 4. Translational updates
    pcm = pcm + Fvector * dt
    rcm = rcm + (pcm / M) * dt

    # 5. Visual updates
    current_thrust_pos = rcm + r_rel
    spacecraft.pos = rcm - vector(0, 0, 0.05)
    thrustpoint.pos = current_thrust_pos
    trail_cm.append(pos=rcm)
    trail_thrust.append(pos=current_thrust_pos)

    t = t + dt