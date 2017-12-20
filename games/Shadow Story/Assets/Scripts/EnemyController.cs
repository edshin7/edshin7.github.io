using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyController : MonoBehaviour {

	public float speed = 6.0f;
	public float gravity = 20.0f;
	public PlayerController playerController;

	private CharacterController controller;
	private Vector3 moveDirection = Vector3.zero;
	private bool faceLeft = true;
	private SpriteRenderer enemySprite;

	// Use this for initialization
	void Start () {
		controller = GetComponent<CharacterController> ();
		enemySprite = gameObject.GetComponentInChildren<SpriteRenderer> ();
	}

	// Update is called once per frame
	void Update () {
		if (faceLeft) {
			moveDirection.x = -speed;
		} else {
			moveDirection.x = speed;
		}

		if (controller.isGrounded) {
			moveDirection.y = 0;
		}

		moveDirection.y -= gravity * Time.deltaTime;
		controller.Move(moveDirection * Time.deltaTime);
	}

	void OnTriggerEnter(Collider other) {
		if (other.gameObject.tag == "turn") {
			faceLeft = !faceLeft;
			enemySprite.flipX = !enemySprite.flipX; 
		}
	}

	void OnControllerColliderHit(ControllerColliderHit hit) {
		if (hit.gameObject.tag == "Player") {
			if (hit.normal.y < -0.5f) {
				DestroyEnemy ();
			} 

			else {
				PlayerController.S.KillPlayer ();
			}
		}
	}

	void DestroyEnemy() {
		controller.enabled = false;
		PlayerController.S.BouncePlayer ();
		GameController.S.PlayCultistAudio ();
		Destroy (this.gameObject);


	}
}
