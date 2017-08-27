using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class CameraController : MonoBehaviour {

	private float addedDepth;

	public GameObject player;
	public float depthUnit;
	public float distUnit;

	// Use this for initialization
	void Start () {
		addedDepth = 0;
	}
	
	// Update is called once per frame
	void Update () {
		Rise ();
		CheckPlayer ();
	}

	// Raises camera height as flood rises
	void Rise () {
		addedDepth += depthUnit;
		transform.Translate (new Vector3(0f, depthUnit, distUnit));

//		if (addedDepth >= 10) {
//			SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
//			print ("Hi");
//		}
	}

	void CheckPlayer () {
		if(!player.activeSelf){
			depthUnit = 0f;
			distUnit = 0f;
		}
	}
}
