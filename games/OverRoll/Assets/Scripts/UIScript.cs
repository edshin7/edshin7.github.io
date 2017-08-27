using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class UIScript : MonoBehaviour {

	public Text bestScore;
	public GameObject soundIcon;
	public Sprite SoundOn;
	public Sprite SoundOff;

	private int curBestScore;

	void Start () {
		curBestScore = PlayerPrefs.GetInt ("Best Score");
		setBestScore ();

		// set sound settings for first time play
		if (!PlayerPrefs.HasKey ("Sound Mode")) {
			PlayerPrefs.SetInt ("Sound Mode", 1);
		} 
			
		updateSoundMode2 ();
		updateBestScore ();

		// show banner ad
		AdManager2.Instance.ShowBanner ();
	}

	// set the best score to 0 if this is the first play
	void setBestScore() {
		if(!PlayerPrefs.HasKey("Best Score")) {
			PlayerPrefs.SetInt ("Best Score", 0);
		}

		bestScore.text = "Best: " + PlayerPrefs.GetInt ("Best Score");
	}

	// update best score when there is a higher one
	void updateBestScore() {
		if (PlayerPrefs.GetInt ("Best Score") > curBestScore) {
			curBestScore = PlayerPrefs.GetInt ("Best Score");
			bestScore.text = "Best: " + curBestScore.ToString();
		}
	}

	// update sound mode to turn on/off
	public void updateSoundMode() {
		Image curImage = soundIcon.GetComponent<Image> ();

		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			PlayerPrefs.SetInt ("Sound Mode", 0);
			curImage.sprite = SoundOff;
		} 

		else {
			PlayerPrefs.SetInt ("Sound Mode", 1);
			curImage.sprite = SoundOn;
		}
	}

	// update sound mode upon loading scene
	void updateSoundMode2() {
		Image curImage = soundIcon.GetComponent<Image> ();

		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			curImage.sprite = SoundOn;
		} 

		else {
			curImage.sprite = SoundOff;
		}
	}

	// play game 
	public void PlayGame() {
		AdManager2.Instance.RemoveBanner ();
		SceneManager.LoadScene ("Game Area");
	}

	// go to info
	public void GetInfo() {
		SceneManager.LoadScene ("Credits");
	}
}
