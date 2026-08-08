using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro; // TextMeshPro kütüphanesini kullanmak için eklenir.

public class GameManager : MonoBehaviour
{

    public static GameManager instance;

    public TextMeshProUGUI scoreText;
    public TextMeshProUGUI timerText;
    public TextMeshProUGUI gameOverText;


    public AudioSource audioSource;
    public AudioClip coinCollectSound;
    public AudioClip gameOverSound;

    private int score = 0;
    public float timer = 10f;
    private bool isGameOver = false;

    // Start is called before the first frame update
    void Awake()
    {
        if (instance == null) instance = this;
        else Destroy(gameObject);
    }

    // Update is called once per frame
    void Update()
    {
        if (!isGameOver)
        {
            if (timer > 0)
            {
                timer -= Time.deltaTime;
                UpdateTimerText();
            }
            else
            {
                timer = 0;
                UpdateTimerText();
                GameOver();
            }
        }
    }

    void UpdateTimerText()
    {
        if (timerText != null)
        {
            timerText.text = "Time: " + Mathf.Ceil(timer).ToString(); 
        }
    }

    public void addScore(int amount)
    {
        if (isGameOver) return;

        score += amount;
        timer += 2f; // her coin toplandığında 2 saniye eklenir. 3.0000000

        if(audioSource != null && coinCollectSound != null)
        {
            audioSource.PlayOneShot(coinCollectSound);
        }

        if (scoreText != null)
        {
            scoreText.text = "Score: " + score.ToString();
        }   
    }

    void GameOver()
    {
        isGameOver = true;
        Debug.Log("Game Over!");
        if(audioSource != null && gameOverSound != null)
        {
            audioSource.PlayOneShot(gameOverSound);
        }
        gameOverText.gameObject.SetActive(true);
    }
}
