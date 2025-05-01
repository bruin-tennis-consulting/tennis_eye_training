using UnityEngine;

public class BallController : MonoBehaviour
{
    public Vector3 initialVelocity = new Vector3(15f, 5f, 0f); 
    public float spinDownwardForce = 5f; // topspin effect (extra downward force)
    public float spinSpeed = 720f; // degrees per second
    public float gravityMultiplier = 1.5f; // custom gravity
    public float airResistanceCoefficient = 0.05f; // tweakable air resistance

    private Rigidbody rb;
    private Vector3 customGravity;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.linearVelocity = initialVelocity; // correct property
        customGravity = Physics.gravity * gravityMultiplier;
    }

    void FixedUpdate()
    {
        // Apply custom gravity (only the extra gravity beyond normal)
        Vector3 extraGravity = customGravity - Physics.gravity;
        rb.AddForce(extraGravity, ForceMode.Acceleration);

        // Apply extra downward force to simulate topspin pull
        Vector3 spinForce = Vector3.down * spinDownwardForce;
        rb.AddForce(spinForce, ForceMode.Acceleration);

        // Apply air resistance (quadratic drag)
        Vector3 airResistanceForce = -airResistanceCoefficient * rb.linearVelocity.sqrMagnitude * rb.linearVelocity.normalized;
        rb.AddForce(airResistanceForce, ForceMode.Force);

        // Rotate the ball visually (topspin spin)
        transform.Rotate(Vector3.right, spinSpeed * Time.fixedDeltaTime, Space.Self);
    }
}

/*
#using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
public class MagnusEffect : MonoBehaviour
{
    public float radius = 0.033f; // meters (real tennis ball radius)
    public float airDensity = 1.225f; // kg/m³ (at sea level)
    public float magnusCoefficient = 0.2f; // Tune this based on how strong you want the effect
    public float dragCoefficient = 0.47f; // Sphere drag coefficient

    private Rigidbody rb;

    void Awake()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        // --- Magnus Effect ---
        Vector3 spin = rb.angularVelocity;
        Vector3 velocity = rb.velocity;
        Vector3 magnusDir = Vector3.Cross(spin, velocity).normalized;
        float magnusForceMag = magnusCoefficient * airDensity * velocity.magnitude * spin.magnitude * Mathf.PI * Mathf.Pow(radius, 3);
        Vector3 magnusForce = magnusForceMag * magnusDir;
        rb.AddForce(magnusForce);

        // --- Air Drag ---
        float area = Mathf.PI * Mathf.Pow(radius, 2); // Cross-sectional area
        float dragMag = 0.5f * dragCoefficient * airDensity * area * velocity.sqrMagnitude;
        Vector3 dragForce = -dragMag * velocity.normalized;
        rb.AddForce(dragForce);
    }
}
public Vector3 windForce = new Vector3(1f, 0f, 0f); // For example
rb.AddForce(windForce);
*/