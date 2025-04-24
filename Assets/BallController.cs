using UnityEngine;

public class BallController : MonoBehaviour
{
    public Vector3 initialVelocity = new Vector3(15f, 5f, 0f); 
    public float spinDownwardForce = 5f; // increased topspin effect
    public float spinSpeed = 720f; // increased spin speed (degrees per second)
    public float gravityMultiplier = 1.5f; // to make it fall faster

    private Rigidbody rb;
    private Vector3 gravity;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.linearVelocity = initialVelocity;
        gravity = Physics.gravity * gravityMultiplier;
    }

    void FixedUpdate()
    {
        // Apply custom gravity for faster fall
        rb.AddForce(gravity, ForceMode.Acceleration);
        
        // Apply extra downward force to simulate topspin
        Vector3 spinForce = Vector3.down * spinDownwardForce;
        rb.AddForce(spinForce, ForceMode.Acceleration);

        // Rotate the ball visually (faster spin)
        transform.Rotate(Vector3.right, spinSpeed * Time.fixedDeltaTime, Space.Self);
    }
}