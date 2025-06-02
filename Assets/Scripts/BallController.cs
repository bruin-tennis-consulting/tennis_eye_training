using UnityEngine;

public class BallController : MonoBehaviour
{
    public Vector3 initialVelocity = new Vector3(0f, 0f, 0f);
    public Vector3 initialAngularVelocity = new Vector3(0f, 0f, 0f); // Use z-direction for current demonstration
    public Vector3 courtTarget = new Vector3(0, 0, 0);
    public float spinConstant = 1f;

    private Rigidbody rb;
    private Vector3 gravity = new Vector3(0f, -9.81f, 0f); // 0x, -9.81y, 0z
    private float ballArea = (Mathf.PI* 1.204f * Mathf.Pow(0.33f, 2.0f)); // Replace 1.204f with ball radius
    bool isGrounded = false;
    private Vector3 previous;

    private 

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        Vector3 ballPos = rb.position;

        // Initial conditions
        rb.linearVelocity = initialVelocity;
        rb.angularVelocity = initialAngularVelocity;
    }


void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Court"))
        {
            rb.angularVelocity *= 0.8f;
        }
    }

    void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.CompareTag("Court"))
        {
            isGrounded = false;
        }
    }

    void FixedUpdate()
    {
        // Apply custom gravity for faster fall
        rb.AddForce(gravity, ForceMode.Acceleration);

        // Apply Rotation?

        // Magnus Force
        if (!isGrounded)
        {
            float C_L = 1.0f / (2.0f + rb.linearVelocity.magnitude / (rb.angularVelocity.magnitude * 0.33f)); // Lift Coefficient
            float F_M = spinConstant * 0.5f * C_L * ballArea * Mathf.Pow(rb.linearVelocity.magnitude, 2.0f); // Implement wind speed later
            Vector3 Force_Magnus = Vector3.Cross(rb.angularVelocity, rb.linearVelocity).normalized * F_M;
            rb.AddForce(Force_Magnus, ForceMode.Acceleration);
        }

        // Drag Force
        float C_d = 0.1f;
        float F_d = 0.5f * C_d * ballArea * Mathf.Pow(rb.linearVelocity.magnitude, 2.0f);
        Vector3 Force_Drag = -1 * rb.linearVelocity.normalized * F_d;
        rb.AddForce(Force_Drag, ForceMode.Acceleration);

        Debug.Log("Vel: " + rb.linearVelocity + "  Angular: " + rb.angularVelocity);
    }
}

/*


Tennis ball. The tennis ball is simulated as a rigid sphere with
the same radius and mass as a real tennis ball, with a restitution
of 0.9 and friction of 0.8. To simulate air friction and the effects of
spin, we add external air drag force 𝐹𝑑 and Magnus force 𝐹𝑀 into
the simulation as follows:
𝐹𝑑 = 𝐶𝑑𝐴𝑣2/2 , 𝐹𝑀 = 𝐶𝐿𝐴𝑣2/2 , (10)
where 𝑣 denotes the magnitude of the ball’s velocity and𝐴 = 𝜋𝜌𝑅2
is
a constant determined by the air density 𝜌 and the ball’s radius 𝑅. 𝐹𝑑
is always opposite to the direction of the ball’s velocity, and𝐶𝑑
refers
to the air drag coefficient, which is set to a constant of 0.55. In tennis,
topspin (forward ball rotation) imparts downward acceleration to
the ball leading it to drop quickly. Backspin (backward ball rotation)
produces upward acceleration causing the ball to float [Brody et al.
2004]. 𝐶𝐿 refers to the lift coefficient due to the Magnus force and
is computed as 1/(2 + 𝑣/𝑣spin) where 𝑣spin denotes the magnitude
of ball’s spin velocity (the relative speed of the surface of the ball
compared to its center point). 𝐹𝑀 is always perpendicular to the
direction of the ball’s angular velocity (following right-hand rule)
and points downwards for topspin and upwards for backspin.


*/
