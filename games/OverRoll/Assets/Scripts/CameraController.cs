using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {

	public GameObject player;
	public float zOffset;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		// move camera with player
		transform.position = new Vector3 (player.transform.position.x, transform.position.y, player.transform.position.z - zOffset);
	}
}
