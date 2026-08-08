using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{

    private Rigidbody2D rigidbody2D; 
    private Vector2 moveInput; //hareket inputu icin
    public float moveSpeed = 5f;



    // Start is called before the first frame update
    void Start()
    {
        rigidbody2D = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        float moveX = Input.GetAxisRaw("Horizontal"); //sağ ve sol kontrolu icin
        float moveY = Input.GetAxisRaw("Vertical"); //yukarı ve aşağı kontrolu icin

        moveInput = new Vector2(moveX, moveY).normalized;  
    }

    void FixedUpdate()
    {
        rigidbody2D.MovePosition(rigidbody2D.position + moveInput * moveSpeed * Time.fixedDeltaTime); //hareketi sabit bir hızda yapar
    } 
}
