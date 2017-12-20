using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TurnCubeBehavior : MonoBehaviour {

	private Renderer rend;

	// Use this for initialization
	void Start () {
		rend = GetComponent<Renderer> ();
		rend.enabled = false;
	}
}
