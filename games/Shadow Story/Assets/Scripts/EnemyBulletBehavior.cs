using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyBulletBehavior : MonoBehaviour {

	public float dir;

	private float speed;
	private Vector3 moveDirection;
	private float timer;
	private CharacterController controller;
	private SpriteRenderer bulletSprite;

	// Use this for initialization
	void Start () {
		speed =  dir * 4.5f;
		moveDirection = new Vector3 (speed, 0.0f, 0.0f);
		timer = 3.0f;

		controller = GetComponent<CharacterController> ();
		bulletSprite = gameObject.GetComponentInChildren<SpriteRenderer> ();

		if (dir == 1.0f) {
			bulletSprite.flipX = true;
		}
	}
	
	// Update is called once per frame
	void Update () {
		controller.Move(moveDirection * Time.deltaTime);
		timer -= Time.deltaTime;

		if (timer <= 0)
			Destroy (this.gameObject);
	}

	void OnTriggerEnter(Collider other) {
		Destroy (this.gameObject);
	}

	void OnControllerColliderHit(ControllerColliderHit hit) {
		if (hit.gameObject.tag == "Player") {
			PlayerController.S.KillPlayer ();
		}

		if(hit.gameObject.tag != "bullet")
			Destroy (this.gameObject);
	}
}
