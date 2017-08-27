using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoverBoundaryScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	void OnTriggerEnter(Collider other) {
		if (other.gameObject.CompareTag ("Player")) {
			other.transform.parent = transform;
		}
	}

	void OnTriggerExit(Collider other) {
		if (other.gameObject.CompareTag ("Player")) {
			other.transform.parent = null;
		}
	}
}
