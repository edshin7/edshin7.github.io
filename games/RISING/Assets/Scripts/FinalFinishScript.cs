using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FinalFinishScript : MonoBehaviour {

	private bool isFinished;
	private float riseSpeed;
	private float riseCount;
	private float riseMax;
	private float rotateSpeedY;
	private float accel;

	public GameObject flood;
	public GameObject cam;
	public Text outcome;

	// Use this for initialization
	void Start () {
		isFinished = false;
		riseSpeed = 0.02f;
		riseCount = 0.0f;
		riseMax = 40.0f;
		rotateSpeedY = 1f;
		accel = 1.15f;
	}
	
	// Update is called once per frame
	void Update () {
		transform.Rotate (new Vector3(0f, rotateSpeedY, 0f));

		if (isFinished && riseCount < riseMax) {
			transform.Translate (new Vector3(0f, riseSpeed, 0f));
			riseSpeed *= accel;
			rotateSpeedY *= accel;
			riseCount++;
		}


	}

	void OnTriggerEnter (Collider other) {
		if(other.gameObject.CompareTag("Player")) {
			other.gameObject.SetActive(false);
			isFinished = true;
			outcome.text = "ESCAPE  SUCCESSFUL";
		}
	}
}
