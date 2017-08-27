using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController2 : MonoBehaviour {

	public GameObject player;
	public float xOffset;
	public float yOffset;
	public float zOffset;

	private Vector3 offset;

	// Use this for initialization
	void Start () {
		offset = new Vector3 (xOffset, yOffset, zOffset);
	}
	
	// Update is called once per frame
	void LateUpdate () {
		transform.position = player.transform.position + offset;
	}
}
