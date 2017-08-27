using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {

	public float jumpSpeed;
	public float walkSpeed;
	public int prizeScore;
	public Text scoreText;
	public Text outcome;
	public Text tryAgain;

	private int score;
	private bool onGround;
	private Rigidbody rb;

	// Use this for initialization
	void Start () {
		score = 0;
		onGround = true;
		rb = GetComponent<Rigidbody> ();
	}
	
	// Update is called once per frame
	void Update () {
		Walk ();
		Jump ();
	}

	void Walk () {
		float moveHorizontal = Input.GetAxis ("Horizontal") * Time.deltaTime * walkSpeed;
		float moveVertical = Input.GetAxis ("Vertical") * Time.deltaTime * walkSpeed;

		transform.Translate (new Vector3(moveHorizontal, 0f, moveVertical));
	}

	void Jump () {
		if (onGround) {
			if (Input.GetButtonDown("Jump")) {
				onGround = false;
				rb.velocity = new Vector3(0f, jumpSpeed, 0f);
			}
		}
	}

	void OnCollisionEnter(Collision other) {
		if (other.gameObject.CompareTag ("Ground") || other.gameObject.CompareTag ("Mover")) {
			onGround = true;
		}
			

		if (other.gameObject.CompareTag ("Enemy")) {
			gameObject.SetActive (false);
			outcome.text = "ESCAPE  FAILED";
			tryAgain.text = "Press R to Restart";
		} 
	}

	void OnTriggerEnter (Collider other) {
		if (other.gameObject.CompareTag ("Flood")) {
			gameObject.SetActive (false);
			outcome.text = "ESCAPE  FAILED";
			tryAgain.text = "Press R to Restart";
		} 

		if (other.gameObject.CompareTag ("Prize")) {
			other.gameObject.SetActive (false);

			score =  score + prizeScore;
			scoreText.text = "Score:  " + score.ToString();
		}

	}
}
