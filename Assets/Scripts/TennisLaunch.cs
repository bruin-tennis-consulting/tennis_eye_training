using UnityEngine;

public static class TennisLaunch
{
    const float RPM2RAD = 2f * Mathf.PI / 60f;

    public static void Fire(Rigidbody rb,
                            Vector3 direction,
                            float speed,
                            Vector3 spinAxis,
                            float rpm)
    {
        rb.linearVelocity = direction.normalized * speed;
        rb.angularVelocity = spinAxis.normalized * rpm * RPM2RAD;
    }
}
