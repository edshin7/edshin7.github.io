using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyCode : MonoBehaviour {

	public float speed;
	public float rotSpeed;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		RotateEnemy ();
	}

	// spin the enemy for a more dynamic view
	void RotateEnemy () {
		transform.Rotate (rotSpeed, rotSpeed, rotSpeed);
	}

	void OnCollisionEnter (Collision other) {
		// destroy enemy if it collides with another enemy, player, or boundary
		if(other.gameObject.CompareTag("Enemy") || other.gameObject.CompareTag("Player") || other.gameObject.CompareTag("Generator")) {
			Destroy(gameObject);
		}
	}
}
