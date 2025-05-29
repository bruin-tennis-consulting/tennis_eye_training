using UnityEngine;

public class Player : MonoBehaviour
{
    public GameObject ballPrefab;
    public Vector3 servePos;


    private void Start()
    {
        // Empty for now...
    }

    void Serve(Vector3 initVel, Vector3 spin)
    {
        GameObject ball = Instantiate(ballPrefab, servePos, Quaternion.identity, transform);
        Rigidbody rb = ball.GetComponent<Rigidbody>();

        if (rb != null)
        {
            rb.linearVelocity = initVel;
        }
    }
}
