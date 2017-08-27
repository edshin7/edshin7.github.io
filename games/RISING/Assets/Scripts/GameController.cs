using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {

	public GameObject player;
	public GameObject finish;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		// if the player is gone, check the conditions
		if (!player.activeSelf) {
			// give restart option if player dies
			if (Input.GetKeyDown (KeyCode.R)) {
				SceneManager.LoadScene (SceneManager.GetActiveScene ().name);
			} 

			// give next level option if player succeeds in Level 1
			else if (!finish.activeSelf && Input.GetKeyDown (KeyCode.N)) {
				if (SceneManager.GetActiveScene ().name != "Level 2") {
					SceneManager.LoadScene ("Level 2");
				}
			}
		}
	}
}
