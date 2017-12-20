using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraControls : MonoBehaviour {

	public GameObject player;

	private float xVelocity = 0.0f;
	private float yVelocity = 0.0f;
	private float yOffset = 0.25f;
	
	// Update is called once per frame
	void Update () {

		Vector3 playerposition = player.transform.position;
		Vector3 cameraposition = transform.position;

		// check for advancing camera

		// move camera with y only if player does not fall below "ground"
		if (playerposition.y > 0.0f) {
			if (cameraposition.x < playerposition.x || cameraposition.x > playerposition.x) {
				cameraposition.x = Mathf.SmoothDamp (cameraposition.x, playerposition.x, ref xVelocity, 0.25f);
			}

			cameraposition.y = Mathf.SmoothDamp (cameraposition.y, playerposition.y, ref yVelocity, 0.25f);
		}

		transform.position = cameraposition;
		
	}
}
