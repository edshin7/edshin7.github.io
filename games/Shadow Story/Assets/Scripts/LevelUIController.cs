using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class LevelUIController : MonoBehaviour {

	private GameObject levelMenu;
	private GameObject gameOver;
	private Text lives;

	// Use this for initialization
	void Start () {
		levelMenu = GameObject.Find ("game menu");
		levelMenu.SetActive (false);

		gameOver = GameObject.Find ("game over");
		gameOver.SetActive (false);

		lives = GameObject.Find ("Lives").GetComponent<Text> ();
	}
	
	// Update is called once per frame
	void Update () {
		lives.text = "Lives: " + GameController.S.GetLives ();
	}

	void SwitchMenu(bool status) {
		levelMenu.SetActive(status);
	}

	public void ResumeGame() {
		Time.timeScale = 1.0f;

		SwitchMenu (false);
	}

	public void Pause() {
		if (!PlayerController.S.GetStillAlive ())
			return;
		
		Time.timeScale = 0.0f;
		SwitchMenu (true);
	}

	// for exiting menu
	public void RestartLevel() {
		string curLevel = SceneManager.GetActiveScene ().name;
		SceneManager.LoadScene (curLevel);
		Time.timeScale = 1.0f;

		SwitchMenu (false);
	}

	public void GameOver() {
		gameOver.SetActive (true);
	}
}
