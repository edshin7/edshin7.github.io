using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class UIScript2 : MonoBehaviour {

	public GameObject menu;
	public GameObject instructions;
	public GameObject soundIcon;
	public Sprite soundOn;
	public Sprite soundOff;

	void Start() {
		Time.timeScale = 0;      // pause to allow player to read instructions
		updateSoundMode2 ();
		menu.SetActive (false);
	}

	public void StartGame() {
		Time.timeScale = 1;
		instructions.SetActive (false);
	}

	public void PauseGame() {
		if (!menu.activeSelf) {
			Time.timeScale = 0;
			menu.SetActive (true);
		}
	}

	public void ResumeGame() {
		if (menu.activeSelf) {
			Time.timeScale = 1;
			menu.SetActive (false);
		}
	}

	public void RestartGame() {
		Time.timeScale = 1;
		SceneManager.LoadScene (SceneManager.GetActiveScene().name);
	}

	public void GoHome() {
		Time.timeScale = 1;
		SceneManager.LoadScene ("Main v2");
	}

	public void GoHome2() {
		if (!PlayerPrefs.HasKey("To Ad Count") || PlayerPrefs.GetInt ("To Ad Count") == 2) {
			PlayerPrefs.SetInt ("To Ad Count", 0);
			AdManager2.Instance.ShowInter ();
		}

		int count = PlayerPrefs.GetInt ("To Ad Count");
		PlayerPrefs.SetInt ("To Ad Count", count + 1);
		GoHome ();
	}

	// update sound mode to turn on/off
	public void updateSoundMode() {
		Image curImage = soundIcon.GetComponent<Image> ();

		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			PlayerPrefs.SetInt ("Sound Mode", 0);
			curImage.sprite = soundOff;
		} 

		else {
			PlayerPrefs.SetInt ("Sound Mode", 1);
			curImage.sprite = soundOn;
		}
	}

	// update sound mode upon loading scene
	public void updateSoundMode2() {
		Image curImage = soundIcon.GetComponent<Image> ();

		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			curImage.sprite = soundOn;
		} 

		else {
			curImage.sprite = soundOff;
		}
	}
}
