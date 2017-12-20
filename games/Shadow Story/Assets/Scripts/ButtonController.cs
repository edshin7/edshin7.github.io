using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ButtonController : MonoBehaviour {

	public void StartMenu() {
		SceneManager.LoadScene ("_Start Menu");
		GameController.S.ResetSpawnPosition ();
		Time.timeScale = 1.0f; // in case player moves from paused state of level back to start menu
	}

	public void StartGame() {
		SceneManager.LoadScene ("Level 1");
		GameController.S.ResetLives (5);
		GameController.S.ResetSpawnPosition ();
	}

	public void DisplayControls() {
		SceneManager.LoadScene ("Controls");
	}

	public void TellStory() {
		SceneManager.LoadScene ("Story");
	}

	public void ExitGame() {
		Application.Quit();
	}

	public void Level2() {
		SceneManager.LoadScene ("Level 2");
		GameController.S.ResetLives (4);
		GameController.S.ResetSpawnPosition ();
	}

	public void Level3() {
		SceneManager.LoadScene ("Level 3");
		GameController.S.ResetLives (3);
		GameController.S.ResetSpawnPosition ();
	}

	public void ShowLevels() {
		SceneManager.LoadScene ("Levels");
	}
}
