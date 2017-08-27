using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// For levels with only one "empty" and units 1X1

public class Movable : MonoBehaviour {

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
		if (Input.GetMouseButtonUp(0) && distance < 6.7 && distance > 6.3) {
			float tempX = transform.position.x;
			float tempZ = transform.position.z;
			transform.position = new Vector3 (empty.transform.position.x, transform.position.y, empty.transform.position.z);
			empty.transform.position = new Vector3 (tempX, empty.transform.position.y, tempZ);
		}
	}
}
