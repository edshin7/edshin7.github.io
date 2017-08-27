using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FloodControl : MonoBehaviour {

	private float addedDepth;

	public float depthUnit;
	public GameObject player;

	// Use this for initialization
	void Start () {
		addedDepth = 0;
	}
	
	// Update is called once per frame
	void Update () {
		Flood ();
		CheckPlayer ();
	}

	// increase scale's y to simulate flood
	void Flood () {
		addedDepth += depthUnit;
		transform.localScale += new Vector3(0f, depthUnit, 0f);
	}

	void CheckPlayer () {
		if(!player.activeSelf){
			depthUnit = 0f;
		}
	}
}
