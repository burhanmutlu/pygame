using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCamera : MonoBehaviour
{
    
    public float followSpeed = 10f;
    public Transform target;
    public Vector3 offset = new Vector3(0, 5f, -10f);


    void LateUpdate()
    {
        if ( target != null)
        {
            Vector3 targetPosition = new Vector3(
                Mathf.Lerp(transform.position.x, target.position.x, 5f * Time.deltaTime),
                target.position.y + offset.y,
                target.position.z + offset.z
            );

            transform.position = Vector3.Lerp(transform.position,targetPosition, followSpeed * Time.deltaTime);
        }
        
    }
}
