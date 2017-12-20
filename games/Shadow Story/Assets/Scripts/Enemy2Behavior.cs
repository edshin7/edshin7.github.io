using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy2Behavior : MonoBehaviour {

	private float speed = 4.0f;
	private bool faceUp = true;
	private Vector3 moveDirection = Vector3.zero;

	private CharacterController controller;

	public PlayerController playerController;

	// Use this for initialization
	void Start () {
		controller = GetComponent<CharacterController> ();
	}

	// Update is called once per frame
	void Update () {
		if (faceUp) {
			moveDirection.y = speed;
		} 

		else {
			moveDirection.y = -speed;
		}

		controller.Move(moveDirection * Time.deltaTime);
	}

	void OnTriggerEnter(Collider other) {
		if (other.gameObject.tag == "turn") {
			faceUp = !faceUp;
		}
	}

	void OnControllerColliderHit(ControllerColliderHit hit) {
		if (hit.gameObject.tag == "Player") {
			PlayerController.S.KillPlayer ();
		}
	}
}
