using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MusicController : MonoBehaviour {

	public AudioSource music;

	// Use this for initialization
	void Start () {
		UpdateSound ();
	}
	
	// Update is called once per frame
	void Update () {
		UpdateSound ();
	}

	void UpdateSound() {
		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			music.mute = false;
		} 
		else {
			music.mute = true;
		}
	}
}
