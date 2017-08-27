using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {

	public float speed;
	public Text finish;

	void Start (){
	}

	void Update (){
		float moveHorizontal = Input.GetAxis ("Horizontal") * Time.deltaTime * speed;
		float moveVertical = Input.GetAxis ("Vertical") * Time.deltaTime * speed;

		transform.Translate (moveHorizontal, 0f, moveVertical);
	}

	void OnTriggerEnter(Collider other) {
		if (other.gameObject.CompareTag ("Finish")) {
			other.gameObject.SetActive (false);
			finish.text = "MAZE COMPLETE";
		}
	}
}
