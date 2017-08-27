using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TileCollision : MonoBehaviour {

	public Text numChanged;
	public Text scoreText;
	public int targetScore;
	public int maxTargetScore;
	public int targetIncrem;
	public Material mat0;
	public Material mat1;
	public Material mat2;
	public Material mat3;
	public AudioClip point;
	public AudioClip reward;
	public AudioClip newRecord;

	private GameObject[] tileObjects;
	private int totalBlackTiles;
	private float totalChangedTiles;
	private int score;
	private int allColorReward;
	private bool newRecordSongPlayed;
	private AudioSource aud;

	void Start () {
		tileObjects = GameObject.FindGameObjectsWithTag ("Tile");
		totalBlackTiles = tileObjects.Length;
		totalChangedTiles = 0.0f;
		score = 0;
		PlayerPrefs.SetInt ("Current Score", score);
		allColorReward = 2;
		newRecordSongPlayed = false;
		aud = gameObject.AddComponent< AudioSource> ();
		aud.volume = 0.3f;
	}

	void Update () {
		UpdateSound ();
	}

	// change Tile color when player collides with Tile
	void OnCollisionEnter (Collision other) {
		if (other.gameObject.CompareTag ("Tile")) {
			
			// add a point once all black tiles are changed
			if (totalBlackTiles <= 0) {
				resetTiles ();
				score += allColorReward;
				PlayerPrefs.SetInt ("Current Score", score);
				scoreText.text = score.ToString ();
				aud.PlayOneShot (reward);
			}

			Renderer rend = other.gameObject.GetComponent <Renderer> ();

			// check if material is mat0 (original black)
			if (rend.sharedMaterial == mat0) {
				totalBlackTiles--;
			}

			// check if the material of the ball != tile material
			if (rend.sharedMaterial != mat1) {
				rend.sharedMaterial = mat1;
				totalChangedTiles++;
				UpdateTiles ();

				numChanged.text = totalChangedTiles.ToString () + "  /  " + targetScore.ToString ();
			}
		}
	}

	// reset tiles to mat0 (original black)
	void resetTiles() {
		foreach(GameObject tile in tileObjects) {
			Renderer rend = tile.GetComponent<Renderer> ();
			rend.sharedMaterial = mat0;
		}

		totalBlackTiles = tileObjects.Length;
	}

	// update Tiles when totalChangedTiles == TargetScore
	void UpdateTiles () {
		if (totalChangedTiles == targetScore) {
			// update score and restart totalChangedTiles
			totalChangedTiles = 0;
			score++;
			PlayerPrefs.SetInt ("Current Score", score);
			scoreText.text = score.ToString ();

			// change materials
			Renderer rend = GetComponent<Renderer> ();
			Material tempMat = mat1;
			rend.sharedMaterial = mat2;
			mat1 = mat2;
			mat2 = mat3;
			mat3 = tempMat;

			// update targetScore
			if (targetScore < maxTargetScore) {
				targetScore += targetIncrem;

				if (!newRecordSongPlayed && score == PlayerPrefs.GetInt ("Best Score") + 1) {
					aud.PlayOneShot (newRecord);
					newRecordSongPlayed = true;
				} 
				else { aud.PlayOneShot (point); }
			}
		}
	}

	// keep track of sound mode
	void UpdateSound() {
		if (PlayerPrefs.GetInt ("Sound Mode") == 1) {
			aud.mute = false;
		} 
		else {
			aud.mute = true;
		}
	}
}
