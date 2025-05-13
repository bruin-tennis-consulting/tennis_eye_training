using UnityEngine;

public class BallController : MonoBehaviour
{
    public Vector3 initialVelocity = new Vector3(0f, 0f, 0f); 
    public float spinDownwardForce = 5f; // increased topspin effect
    public float spinSpeed = 720f; // increased spin speed (degrees per second)
    public Vector3 courtTarget = new Vector3(0, 0, 0);

    private Rigidbody rb;
    private Vector3 gravity = new Vector3(0f, -9.81f, 0f); // 0x, -9.81y, 0z

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        Vector3 ballPos = rb.position;
        //Vector3 dir = (courtTarget - ballPos).normalized;
        rb.velocity = initialVelocity;



    }

    void FixedUpdate()
    {
        // Apply custom gravity for faster fall
        rb.AddForce(gravity, ForceMode.Acceleration);

        // Handle Rotation
        // transform.Rotate(Vector3.right, spinSpeed * Time.fixedDeltaTime, Space.Self);
    }
}


/*
 
CHECKLIST:
1. Mass     DONE
2. Sphere Collider(radius?)      DONE
3. Continuous Dynamic collision detection      DONE
4. Time step ≤ 0.005 s to avoid tunnelling      DONE
5. Physic Material on ball & court (bounciness ≈ 0.74, frictions tuned per surface)
6. Gravity (–9.81 m s⁻²)
7. Quadratic air drag ½ ρ Cd A v²
8. Magnus / lift force ½ ρ Cl A v² (ω̂ × v̂)
9. Spin-decay in air (felt + viscosity)


*/
