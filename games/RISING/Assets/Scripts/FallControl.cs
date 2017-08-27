using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FallControl : MonoBehaviour {

	private bool isTouched;
	private float fallSpeed;

	// Use this for initialization
	void Start () {
		isTouched = false;
		fallSpeed = -0.01f;
	}
	
	// Update is called once per frame
	void Update () {
		Fall ();
	}

	void Fall() {
		if(isTouched) {
			transform.Translate(new Vector3(0f, fallSpeed, 0f));
		}
	}

	void OnCollisionEnter(Collision other) {
		if(other.gameObject.CompareTag("Player")) {
				isTouched = true;
			}
	}
}
