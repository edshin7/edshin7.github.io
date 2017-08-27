using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PrizeScript : MonoBehaviour {

	public float rotateSpeedY;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		transform.Rotate(new Vector3(0f, rotateSpeedY, 0f));
	}
}
