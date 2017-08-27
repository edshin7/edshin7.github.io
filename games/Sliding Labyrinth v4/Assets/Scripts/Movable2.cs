using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// For levels with only one "empty" and units 1X2

public class Movable2 : MonoBehaviour {

	public GameObject empty;

	// Use this for initialization
	void Start () {
//		empty = GameObject.Find ("Empty");
	}

	// Update is called once per frame
	void Update () {
	}

	void OnMouseUp(){
		float distance = Vector3.Distance (transform.position, empty.transform.position);
		if (Input.GetMouseButtonUp(0) && distance < 9.8 && distance > 9.7) {
			float dist = transform.position.x - empty.transform.position.x;
			float dir = dist / Mathf.Abs (dist);
			float newXUnit = (float)(empty.transform.position.x + (dir * 3.25));
			float newXEmpty = (float)(transform.position.x + (dir * 3.25));

			transform.position = new Vector3 (newXUnit, transform.position.y, transform.position.z);
			empty.transform.position = new Vector3 (newXEmpty, empty.transform.position.y, empty.transform.position.z);
		}
	}
}
