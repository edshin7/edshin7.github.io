using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class DiagControl : MonoBehaviour, IPointerDownHandler {

	public PlayerController playerControl;
	public float direction;

	// Use this for initialization
	void Start () {
		
	}

	public void OnPointerDown(PointerEventData eventData)
	{
		playerControl.RotateDirection(direction);
	}
}
