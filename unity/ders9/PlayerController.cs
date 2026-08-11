using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{

    public float forwardSpeed = 12f;
    public float maxVelocity = 25f;

    public float swerveSpeed = 5f;
    public float maxSwerveX = 4.5f;

    private Rigidbody rb;
    private float lastFrameFingerX;
    private float moveX;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.maxAngularVelocity = 50f;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            lastFrameFingerX = Input.mousePosition.x;
        }
        else if(Input.GetMouseButton(0))
        {
            moveX = Input.mousePosition.x - lastFrameFingerX;
            lastFrameFingerX = Input.mousePosition.x;
        }
        else if(Input.GetMouseButtonUp(0))
        {
            moveX = 0;
        }
    }

    void FixedUpdate()
    {
        if(rb.velocity.magnitude < maxVelocity)
        {
            rb.AddForce(Vector3.forward * forwardSpeed, ForceMode.Acceleration);
        }

        float swerveAmount = moveX * swerveSpeed * Time.fixedDeltaTime;
        Vector3 currentPosition = transform.position;

        Vector3 newPosition = new Vector3(
            Mathf.Clamp(currentPosition.x + swerveAmount, -maxSwerveX, maxSwerveX),
            currentPosition.y,
            currentPosition.z
        );
        rb.MovePosition(newPosition);

        moveX = 0;
    }
}
