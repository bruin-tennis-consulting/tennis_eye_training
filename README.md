#  Tennis Eye Training

A realistic Unity-based simulator that helps tennis players train their perception of ball spin bounce and trajectory. Developed by Bruin Tennis Consulting this project leverages Unitys physics engine and custom scripts to simulate game-like tennis ball behavior with a focus on spin dynamics bounce realism and player feedback.

---

##  Project Goals

- Model realistic tennis ball physics including Magnus effect and angular momentum.
- Create an immersive visual simulation to train anticipation and reaction to spin and bounce.
- Enable easy tuning and extension for research training or competitive analysis.

---

##  Features

-  Unity Rigidbody physics integration  
-  Accurate spin-to-bounce behavior (topspin slice flat)
-  Magnus effect simulation for realistic arc curves  
-  Modular ball control scripts (e.g. `BallController.cs`)  
-  Court target placement and trajectory control  
-  Adjustable parameters for drag mass damping and friction

---

##  Project Structure

```
tennis_eye_training/
 Assets/
    Scripts/
       BallController.cs     # Controls spin Magnus effect trajectory
    Materials/                # Physic materials for ball and court
    Scenes/                   # Unity scenes for testing and demos
    Prefabs/                  # Reusable ball/court prefabs
 README.md
```

---

##  Getting Started

### Prerequisites

- Unity 2022.x or newer
- Physics Materials set up on
  - Tennis Ball (e.g. with low bounciness and tuned friction)
  - Court (high friction no bounce)

### Running the Simulation

1. Clone the repository

   ```bash
   git clone https//github.com/bruin-tennis-consulting/tennis_eye_training.git
   cd tennis_eye_training
   ```

2. Open the project in Unity Hub.

3. Load the main scene under `Assets/Scenes/`.

4. Play the scene to test trajectory and bounce behavior.

---

##  Customization

Adjust these variables in `BallController.cs`

```csharp
public Vector3 initialVelocity      // Launch speed and direction
public Vector3 initialAngularVelocity  // Spin direction and rate
public Vector3 courtTarget          // Desired impact location
```

You can also modify

- Rigidbody drag mass and angular drag
- Physics materials (friction bounciness)
- Air resistance model for advanced spin decay

---

##  Known Issues

- Spin direction may invert unrealistically on bounce  
- Some bouncing behavior appears exaggerated due to Unitys default physics  
- Work in progress on post-bounce spin decay and friction loss

---

##  Contributing

Pull requests are welcome Please open an issue first if youd like to discuss a feature or bug fix. Were especially interested in

- Physics tuning experts
- Computer vision researchers for video training input
- UI/UX contributors for training feedback overlays

---

##  License

This project is licensed under the MIT License.

---

##  Authors

Developed by the [Bruin Tennis Consulting](https//github.com/bruin-tennis-consulting) team.  
Lead: Jayden Spurgiasz
PM: Kevin Cao
Contributors: Jerry Shi, Jason Fan, Collin MacPherson
