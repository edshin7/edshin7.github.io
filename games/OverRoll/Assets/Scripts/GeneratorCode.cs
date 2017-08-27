using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GeneratorCode : MonoBehaviour {

	public GameObject enemy;
	public Transform front;

	private float minForce; // minimum force for launching enemy
	private float maxForce; // maximum force for launching enemy
	private float chance;   // chance of launching an enemy
	private float chanceInc;  // increment to increase chance of generating with increasing difficulty
	private float maxChance;
	private int target;  // target score at which to increase chance
	private int targetInc;
	private int targetFrame;  // target frame count at which to generate enemies

	void Start () {
		minForce = 150.0f;
		maxForce = 200.0f;
		chance = 0.002f;
		chanceInc = 0.001f;
		maxChance = 0.016f;
		target = targetInc = 3;
		targetFrame = 10;
	}
	
	void Update () {
		makeEnemy ();
		UpdateChance ();
	}

	// make an enemy with random speeds at random times
	void makeEnemy () {
		float rand = Random.value;

		// make an Enemy if rand <= chance
		if (Time.timeScale == 1 && Time.frameCount % targetFrame == 0 && rand <= chance) {
			float enemyForce = Random.Range (minForce, maxForce);
			GameObject clone;

			print ("hi");
			clone = Instantiate (enemy, front.position, front.rotation);

			Rigidbody rb = clone.GetComponent<Rigidbody> ();
			rb.AddForce (front.forward * enemyForce);
		}
	}

	// update chance for increased difficulty
	void UpdateChance() {
		if (PlayerPrefs.GetInt ("Current Score") == target && chance < maxChance) {
			target += targetInc;
			chance += chanceInc;
		}
	}
}
