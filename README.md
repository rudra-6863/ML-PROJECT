# ML-PROJECT
## 🔧 **ML-Based Wheel RPM Prediction for Turning Robot**

---

### 📌 **Project Title:**
**"Machine Learning Model for Predicting Wheel RPMs Based on Robot Turning Angle"**

---

### 🎯 **Objective:**

To build a **machine learning model** that predicts the **left and right wheel RPMs** required for a differential-drive robot to perform a smooth **arc-based turn**, based on a given **steering angle**.

The model will:
- Take **input** as the turn angle (within -30° to +30°).
- Predict the **RPM** of the **left and right motors**.
- Estimate the **time** and **distance** the robot will travel during the turn.

---

### ⚙️ **System Assumptions and Constants:**
- **Wheelbase (d)**: 0.2 meters (distance between wheels)
- **Wheel radius (r)**: 0.03 meters
- **Forward speed (V)**: 0.2 m/s (constant speed)
- **Angle Range Limit**: -30° to +30° allowed for safety and accuracy

---

### 🔣 **Mathematical Background:**

The robot uses **differential drive kinematics** to move in an arc. For a given angle `θ`, the robot calculates:

1. **Turning Radius (R):**
   \[
   R = \frac{1}{\tan(\theta)}
   \]

2. **Left and Right Linear Velocities:**
   \[
   V_l = V \cdot \left(1 - \frac{d}{2R}\right), \quad V_r = V \cdot \left(1 + \frac{d}{2R}\right)
   \]

3. **Convert to RPM:**
   \[
   \text{RPM}_l = \left(\frac{V_l}{2\pi r}\right) \cdot 60, \quad \text{RPM}_r = \left(\frac{V_r}{2\pi r}\right) \cdot 60
   \]

---

### 🧠 **Machine Learning Model:**

- **Algorithm Used**: Linear Regression (from `scikit-learn`)
- **Input (X)**: Turn angle (in degrees)
- **Output (y)**: Predicted `[left_wheel_rpm, right_wheel_rpm]`

---

### 🗃️ **Dataset Generation:**

Synthetic data is generated using the `arc_rpm()` function:
- **Input Angles**: from -60° to +60° (to ensure enough training data)
- **Target Outputs**: RPMs computed from physics model

Only angles between **-30° to +30°** are **accepted for predictions**, ensuring safety and real-world reliability.

---

### 🧪 **Testing and Input Validation:**

- The model takes a user-provided input angle.
- Validates if it lies within the range [-30°, +30°].
- If **valid**:
  - Predicts left/right RPMs.
  - Calculates turning **radius**, **arc length**, and **time** needed to complete the turn.
- If **invalid**:
  - Shows an error message.

---

### 📈 **Visualization:**

The model plots:
- True RPMs (from physical model)
- Predicted RPMs (from ML model)
- Shows alignment between learned behavior and actual physics
- Vertical lines show the valid input range (±30°)

---

### 📊 **Output Example (if angle = 20°):**

```
Angle: 29.0°
Predicted Left RPM: 59.37
Predicted Right RPM: 67.95
Estimated Time to complete turn: 4.57 seconds
Estimated Distance traveled during turn: 0.91 meters
```

---

### ✅ **Applications:**
- **Line-following robots**
- **Autonomous navigation**
- **Smooth arc-turning path planning**
- **Differential drive simulations and training**

---

### 🚀 **Future Improvements:**
- Use **non-linear ML models** (like Polynomial Regression, Neural Networks) for better accuracy.
- Integrate real sensor data to train on actual robot behavior.
- Add **real-time control interface** to test predictions with hardware.

---
