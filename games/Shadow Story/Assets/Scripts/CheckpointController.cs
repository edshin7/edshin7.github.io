using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CheckpointController : MonoBehaviour {

	public Sprite checkOn;
	public Sprite checkOff;

	private bool checkIsOn = false;
	private SpriteRenderer checkpointRend;
	private AudioSource checkAudio;

	// Use this for initialization
	void Start () {
		checkpointRend = GetComponentInChildren<SpriteRenderer> ();
		checkAudio = GetComponent<AudioSource> ();
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void turnCheckOn() {
		checkAudio.Play ();
		checkIsOn = true;
		checkpointRend.sprite = checkOn;
	}

	public void turnCheckOff() {
		checkIsOn = false;
		checkpointRend.sprite = checkOff;
	}
}
