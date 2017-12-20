using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

	public float speed = 6.0F;
	public float jumpSpeed = 8.0F;
	public float gravity = 20.0F;

	private Vector3 moveDirection = Vector3.zero;

	private CharacterController controller;
	private GameObject gameCamera;
	private Animator animator;
	private SpriteRenderer playerSprite;

	private bool faceRight = true;
	private bool stillAlive = true;

	private float respawnTime = 3.0f;
	private float timer = 3.0f;

	private bool gameIsOver = false;

	private float fallDeathDepth = -6.5f;
	private bool playerFell = false;

	private GameObject curCheck = null;
	private GoalBehavior goal;

	private AudioSource playerAudio;

	static public PlayerController S;

	void Start() {
		controller = GetComponent<CharacterController>();
		gameCamera = GameObject.FindGameObjectWithTag ("MainCamera");
		animator = GetComponent<Animator> ();
		playerSprite = GetComponent<SpriteRenderer> ();
		playerAudio = GetComponent<AudioSource> ();

		if(goal != null)
			goal = GameObject.Find ("goal").GetComponent<GoalBehavior> ();

		S = this;

		GameController.S.ResetSpawnPosition ();
	}

	void Update() {
		MovePlayer ();
		CheckPlayerFall ();
		RespawnPlayer ();
	}

	void MovePlayer() {
		if (controller.enabled && stillAlive) {
			if (controller.isGrounded) {
				moveDirection = new Vector3 (Input.GetAxis ("Horizontal"), 0, 0);
				moveDirection *= speed;
				if (Input.GetButton ("Jump"))
					moveDirection.y = jumpSpeed;

			} else {
				moveDirection.x += Input.GetAxis ("Horizontal") * 0.2f;
				moveDirection.x = Mathf.Clamp (moveDirection.x, -speed, speed);

			}
			moveDirection.y -= gravity * Time.deltaTime;
			controller.Move (moveDirection * Time.deltaTime);

		}

			// set animator values
			animator.SetBool("grounded", controller.isGrounded);
			animator.SetFloat ("speed", Mathf.Abs(Input.GetAxis ("Horizontal")));
			animator.SetBool ("alive", stillAlive);

		if (controller.enabled && stillAlive) {
			// sprite direction
			if ((Input.GetAxis ("Horizontal") < 0) && faceRight) {
				playerSprite.flipX = true;
				faceRight = false;
			} else if ((Input.GetAxis ("Horizontal") > 0) && !faceRight) {
				faceRight = true;
				playerSprite.flipX = false;
			}
		}
	}

	void RespawnPlayer() {
		if (stillAlive)
			return;

		if (GameController.S.GetLives () == 0) {
			if (gameIsOver)
				return;

			LevelUIController levelUI = GameObject.Find ("Level UI").GetComponent<LevelUIController>();
			levelUI.GameOver();
			gameIsOver = true;
			return;
		}

		timer -= Time.deltaTime;

		if (timer <= 0.0f) {
			GameController.S.ResetLevel ();

			timer = respawnTime;

			playerFell = false;
			stillAlive = true;
			controller.enabled = true;


		}
	}


	// check if player fell to death
	void CheckPlayerFall() {
		if (!playerFell && gameObject.transform.position.y <= fallDeathDepth) {
			playerFell = true;
			KillPlayer ();
		}
	}

	public bool GetStillAlive() {
		return stillAlive;
	}

	void OnControllerColliderHit(ControllerColliderHit hit)
	{
		if (hit.moveDirection == Vector3.up) {
			if ((hit.transform.tag == "Platform") && (moveDirection.y > -1.0f)) {
				Debug.Log (hit.transform.tag);
				moveDirection.y = -1.0f;

				if(!stillAlive)
					controller.enabled = false;
			}
		}

		if (hit.gameObject.tag == "wisp" || hit.gameObject.tag == "bullet") {
			S.KillPlayer ();
		}
	}

	void OnTriggerEnter(Collider other) {
		if (other.gameObject.tag == "goal") {
			GoalBehavior goalScript = other.gameObject.GetComponent<GoalBehavior> ();

			if (goalScript.getIsOpen ()) {
				GameController.S.PlayGoalAudio ();
				goalScript.AdvanceLevel ();
			}
		} 

		else if (other.gameObject.tag == "checkpoint" && !other.Equals(curCheck)) {
			if (curCheck != null) {
				CheckpointController c = curCheck.GetComponent<CheckpointController> ();
				c.turnCheckOff ();
			}

			curCheck = other.gameObject;
			CheckpointController c2 = curCheck.GetComponent<CheckpointController> ();

			c2 = curCheck.GetComponent<CheckpointController>();
			c2.turnCheckOn ();

			GameController.S.ResetSpawnPosition ();
		}

		else if (other.gameObject.tag == "key") {
			other.gameObject.SetActive(false);

			if(goal != null)
				goal.CheckForKeys ();
		}
	}

	public void BouncePlayer() {
		moveDirection.y = 12.0f;
	}

	public void KillPlayer() {
		if(stillAlive) {
			playerAudio.Play ();
			GameController.S.MinusLives ();
			stillAlive = false;
			controller.enabled = false;
		}
	}

}
