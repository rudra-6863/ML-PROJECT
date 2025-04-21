import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Constants
d = 0.2   # Wheelbase (m)
r = 0.03  # Wheel radius (m)
V = 0.2   # Forward speed (m/s)
MAX_ANGLE = 30  # allowed turn angle limit

# Function to generate RPMs while turning
def arc_rpm(theta):
    if theta == 0:
        return V, V  # straight motion
    R = 1.0 / (np.tan(np.radians(theta)) + 1e-6)  # radius of curvature
    Vl = V * (1 - (d / (2 * R)))
    Vr = V * (1 + (d / (2 * R)))
    rpm_l = (Vl / (2 * np.pi * r)) * 60
    rpm_r = (Vr / (2 * np.pi * r)) * 60
    return rpm_l, rpm_r

# Dataset
angles = np.linspace(-60, 60, 200)  # larger set to train, but input will be restricted
rpm_data = np.array([arc_rpm(theta) for theta in angles])
X = angles.reshape(-1, 1)
y = rpm_data

# Train ML model
model = LinearRegression()
model.fit(X, y)

# Input with validation
try:
    test_angle = float(input("Enter value of angle (-30° to 30°): "))
    
    if not -MAX_ANGLE <= test_angle <= MAX_ANGLE:
        raise ValueError(f"Error: Angle must be between -{MAX_ANGLE}° and {MAX_ANGLE}°")

    # Predict RPMs
    predicted = model.predict([[test_angle]])
    print(f"\nAngle: {test_angle}°")
    print(f"Predicted Left RPM: {predicted[0][0]:.2f}")
    print(f"Predicted Right RPM: {predicted[0][1]:.2f}")

    # Estimate turn radius and arc length
    R = abs(1.0 / (np.tan(np.radians(test_angle)) + 1e-6))  # prevent div by zero
    angle_rad = np.radians(abs(test_angle))  # in radians
    arc_length = R * angle_rad              # distance robot travels
    time_required = arc_length / V          # time = distance / speed

    print(f"Estimated Time to complete turn: {time_required:.2f} seconds")
    print(f"Estimated Distance traveled during turn: {arc_length:.2f} meters")

except ValueError as e:
    print(e)

# Plotting the whole trained range for visualization
plt.plot(angles, y[:, 0], label='True Left RPM')
plt.plot(angles, y[:, 1], label='True Right RPM')
plt.plot(angles, model.predict(X)[:, 0], '--', label='Pred Left RPM')
plt.plot(angles, model.predict(X)[:, 1], '--', label='Pred Right RPM')
plt.axvline(x=-30, color='r', linestyle=':', label='Allowed Range')
plt.axvline(x=30, color='r', linestyle=':')
plt.xlabel('Turn Angle (°)')
plt.ylabel('Wheel RPM')
plt.title('Wheel RPMs vs Turning Angle')
plt.legend()
plt.grid(True)
plt.show()