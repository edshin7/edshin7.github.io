using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {

	private int curLevel = 0;
	private int playerLives = 5;

	private GameObject player;
	private GameObject gameCamera;
	private Vector3 spawnPosition;

	private AudioSource cultistAudio;
	private AudioSource goalAudio;

	public static GameController S;

	// Use this for initialization
	void Start () {
		cultistAudio = GetComponents<AudioSource> () [1];
		goalAudio = GetComponents<AudioSource> () [2];
		// check for the singleton
		if (GameController.S != null) {
			// singleton already exists.  destroy this object and cease execution of script
			Destroy (this.gameObject);
			return;
		}

		// We only arrive here if no singleton has been set, so now we define it.
		S = this;
		DontDestroyOnLoad (this);

		ResetSpawnPosition ();

	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public int GetLives() {
		return playerLives;
	}

	public void MinusLives() {
		playerLives--;
	}

	public void PlusLives() {
		playerLives++;
	}

	public void ResetLives(int numLives) {
		playerLives = numLives;
	}

	public void ResetSpawnPosition() {
		player = GameObject.FindGameObjectWithTag ("Player");

		if (player == null)
			return; 
		
		gameCamera = GameObject.Find ("Main Camera");
		spawnPosition = player.gameObject.transform.position;
	}

	// restarting at a designated point after dying
	public void ResetLevel() {
		player.gameObject.transform.position = spawnPosition;
		gameCamera.gameObject.transform.position = new Vector3(spawnPosition.x, spawnPosition.y, 
			gameCamera.gameObject.transform.position.z);
	}

	public void PlayCultistAudio() {
		cultistAudio.Play ();
	}

	public void PlayGoalAudio() {
		goalAudio.Play ();
	}
}
