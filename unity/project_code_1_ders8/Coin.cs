using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Coin : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // ilk başlatma işlemleri burada yapılır
    }

    private void OnTriggerEnter2D(Collider2D c)
    {
        if (c.CompareTag("Player"))
        {
            RelocateCoin();
            GameManager.instance.addScore(5); // her coin toplandığında 1 puan eklenir.
        }
    }

    void RelocateCoin()
    {
        float randomX = Random.Range(-8f, 8f);
        float randomY = Random.Range(-4f, 4f);
        transform.position = new Vector2(randomX, randomY);
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(0f,0f, 50 * Time.deltaTime); // coin objesini döndürmek için kullanılır. 50 derece/saniye hızıyla döndürür.

        float newY = Mathf.Sin(Time.time * 5f) * 0.001f; // coin objesini yukarı ve aşağı hareket ettirmek için kullanılır. 2 saniyede bir tam tur yapar ve 0.5 birim yukarı ve aşağı hareket eder.
        transform.position = new Vector3(transform.position.x, transform.position.y + newY, transform.position.z);
    }
}
