using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {

	public float speed;
	public GameObject gameOver;
	public Text scoreText;
	public Text score;
	public Text bestScore;
	public AudioClip destroy;
	public ParticleSystem particle;

	private float shrinkInc;
	private float minSize;
	private bool isHit;  // tells when ball is hit
	private bool isGone;   // tells when ball has Shrunken
	private AudioSource aud;

	// Use this for initialization
	void Start () {
		shrinkInc = 0.023f;
		minSize = 0.01f;
		aud = gameObject.AddComponent<AudioSource> ();
		aud.volume = 0.3f;
		gameOver.SetActive(false);
	}
	
	// Update is called once per frame
	void Update () {
		Roll2 ();
		EndGame ();
		UpdateSound ();
	}

	void Roll2 () {
		float moveVertical = Time.deltaTime * speed;
		transform.Translate (new Vector3(0f, 0f, moveVertical));
	}

	// set the direction of the player to a certain direction
	public void RotateDirection (float angle) {
		transform.eulerAngles = new Vector3(0f, angle, 0f);
	}

	void OnCollisionEnter (Collision other) {
		// deactivate player and end the game when player collides with Bottom or Enemy
		// scores will be displayed and best scores will be updated as appropriate
		if(other.gameObject.CompareTag("Bottom") || other.gameObject.CompareTag("Enemy")) {
			// stop movement and shrink and play music
			if (!isHit) { aud.PlayOneShot (destroy); }

			Rigidbody playRigid = gameObject.GetComponent<Rigidbody> ();
			playRigid.isKinematic = true;
			playRigid.detectCollisions = false;    // make sure nothing else physically collides into defeated player


			particle.gameObject.transform.position = gameObject.transform.position;
			Renderer partRend = particle.GetComponent<Renderer> ();
			Renderer playRend = gameObject.GetComponent<Renderer> ();
			partRend.sharedMaterial = playRend.sharedMaterial;
			particle.Play ();

			speed = 0.0f;
			isHit = true;
		}
	}

	void EndGame() {
		// when player is hit by enemy, shrink until it reaches small size
		if (isHit) {
			if (gameObject.transform.localScale.x > minSize && !isGone) {
				gameObject.transform.localScale -= new Vector3 (shrinkInc, shrinkInc, shrinkInc);
			} 

			else { isGone = true; }
		}

		// once player reaches small size, turn it off and display game over screen
		if (isGone && !gameOver.activeSelf) {
			gameOver.SetActive(true);
			scoreText.text = "Score: " + score.text;

			if (PlayerPrefs.GetInt ("Current Score") > PlayerPrefs.GetInt ("Best Score")) {
				PlayerPrefs.SetInt ("Best Score", PlayerPrefs.GetInt ("Current Score"));
				bestScore.text = "NEW RECORD!";
			} 

			else {
				bestScore.text = "Best: " + PlayerPrefs.GetInt ("Best Score").ToString();
			}

			gameObject.SetActive (false);
		}
	}

	// keep track of sound mode
	void UpdateSound() {
		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			aud.mute = false;
		} 
		else { aud.mute = true; }
	}
}
