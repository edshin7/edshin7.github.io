using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour {

	public float rotateSpeedX;
	public float rotateSpeedY;
	public float rotateSpeedZ;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		transform.Rotate (new Vector3(rotateSpeedX, rotateSpeedY, rotateSpeedZ));
	}
}
