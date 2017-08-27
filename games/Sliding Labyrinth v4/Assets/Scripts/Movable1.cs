using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// for levels with multiple "empty"s and 1X2 units

public class Movable1 : MonoBehaviour {

	public string unitType;

	private GameObject[] emptys;

	// Use this for initialization
	void Start () {
		emptys = GameObject.FindGameObjectsWithTag ("Empty");
	}

	// Update is called once per frame
	void Update () {
	}

	void OnMouseUp(){
		foreach (GameObject empty in emptys) {
			float distance = Vector3.Distance (transform.position, empty.transform.position);

			if (Input.GetMouseButtonUp(0) && distance < 9.8 && distance > 9.7) {
				float tempX = transform.position.x;
				float tempZ = transform.position.z;

				if(unitType == "1X2 Horizontal") {

					float dist = transform.position.x - empty.transform.position.x;
					float dir = dist / Mathf.Abs (dist);
					float newXUnit = (float)(empty.transform.position.x + (dir * 3.25));
					float newXEmpty = (float)(transform.position.x + (dir * 3.25));
					
					transform.position = new Vector3 (newXUnit, transform.position.y, transform.position.z);
					empty.transform.position = new Vector3 (newXEmpty, empty.transform.position.y, empty.transform.position.z);
				}

				else if(unitType == "1X2 Vertical") {

					float dist = transform.position.z - empty.transform.position.z;
					float dir = dist / Mathf.Abs (dist);
					float newZUnit = (float)(empty.transform.position.z + (dir * 3.25));
					float newZEmpty = (float)(transform.position.z + (dir * 3.25));

					transform.position = new Vector3 (transform.position.x, transform.position.y, newZUnit);
					empty.transform.position = new Vector3 (empty.transform.position.x, empty.transform.position.y, newZEmpty);
				}
			}
		}
	}
}
