using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GoalBehavior : MonoBehaviour {

	public string nextLevel;
	public bool isOpen;
	public Sprite closed;
	public Sprite opened;

	private SpriteRenderer goalSprite;
	private GameObject[] keys;
	private int numKeys;

	void Start () {
		goalSprite = gameObject.GetComponentInChildren<SpriteRenderer> ();
		keys = GameObject.FindGameObjectsWithTag ("key");
		numKeys = keys.Length;

		if (!isOpen)
			goalSprite.sprite = closed;
	}

	void Update () {
		
	}

	// if there are no keys, unlock the goal
	public void CheckForKeys() {
		numKeys--;

		if (numKeys == 0) {
			isOpen = true;
			goalSprite.sprite = opened;
		}
	}


	public void AdvanceLevel() {
		SceneManager.LoadScene (nextLevel);
	}

	public bool getIsOpen() {
		return isOpen;
	}

	public void UnLockGoal() {
		isOpen = true;
	}

}
