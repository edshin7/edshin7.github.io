using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoverScript : MonoBehaviour {

	public string direction;
	public float speed;
	public float totalDistance;
	public float traveledDistance;

	private Vector3 vector;


	// Use this for initialization
	void Start () {
		setVector ();
	}
	
	// Update is called once per frame
	void Update () {
		transform.Translate (vector);
		traveledDistance = traveledDistance + Mathf.Abs(speed);

		if (traveledDistance >= totalDistance) {
			speed = -speed;
			traveledDistance = 0f;
			setVector();
		}
	}

	void setVector() {
		if (direction == "x" || direction == "X") {
			vector = new Vector3 (speed, 0f, 0f);
		} 

		else if (direction == "y" || direction == "Y") {
			vector = new Vector3 (0f, speed, 0f);
		} 

		else if (direction == "z" || direction == "Z") {
			vector = new Vector3 (0f, 0f, speed);
		}
	}
		
}
