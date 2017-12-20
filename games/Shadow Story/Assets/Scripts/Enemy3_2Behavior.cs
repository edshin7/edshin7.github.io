using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy3_2Behavior : MonoBehaviour {

	private float timer;
	public GameObject bullet;

	// Use this for initialization
	void Start () {
		timer = 3.0f;
	}
	
	// Update is called once per frame
	void Update () {
		timer -= Time.deltaTime;
		if(timer <= 0.0f) {
			Instantiate (bullet, new Vector3(transform.position.x + 1.0f, transform.position.y, transform.position.z), Quaternion.identity);
			timer = 3.0f;
		}
	}
}
