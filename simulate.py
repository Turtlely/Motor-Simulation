import config
import numpy as np
import matplotlib.pyplot as plt

time = []
angles = []

#Start the coil off parallel to the B field
theta = 0
Tglob = 0
dt = 0.001
v=0


while Tglob <= 100:
    # Calculate the force that the motor feels
    F = config.I * config.L * config.B

    # Calculate the torque
    T = 2 * F * config.R * np.cos(theta)

    # Calculate moment of inertia
    I = config.M * config.R**2

    # Calculate the angular acceleration
    a = T/I

    '''Eulers Method for solving the differential equation'''
    # Calculate the new angle after time step dt
    v+= a * dt
    theta += v * dt
    Tglob+=dt
    time.append(Tglob)
    angles.append(np.rad2deg(theta)/360)

    # Commutator simulator

    # Calculate reference angle in a loop
    testangle = theta
    while testangle > 2* np.pi :
        testangle = testangle - 2*np.pi

    if testangle > np.pi/2:
        #Flip current direction
        config.I = np.abs(config.I)*-1
    if testangle < np.pi/2:
        config.I = np.abs(config.I)

# Calculate angular velocity of motor
out = np.polyfit(time,angles,2)

# Plot line of best fit
y = out[0]*np.square(time) + out[1]*np.float64(time) + out[2]

print("Angular Acceleration (rev/s2): ", 2*out[0])

fig= plt.figure()
ax = fig.add_subplot(111)

# Plot angle over time
ax.set_ylabel("Rotations Made")
ax.set_xlabel("Time (Seconds) ")

ax.plot(time,angles,c='blue')
ax.plot(time,y,c='red')

plt.grid(True)
plt.title("Motor Simulation with a commutator, α = " + str(round(2*out[0],2)) + " rev/s2")
plt.show()