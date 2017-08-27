using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using admob;

public class AdManager2 : MonoBehaviour {

	public static AdManager2 Instance { set; get; }

	private string bannerId;
	private string interId;

	private void Start() {
		Instance = this;
		DontDestroyOnLoad (gameObject);

		bannerId = "ca-app-pub-5280137635299744/4106654568";
		interId = "ca-app-pub-5280137635299744/5278111918";

		#if UNITY_EDITOR
		#elif UNITY_ANDROID

		Admob.Instance ().initAdmob(bannerId, interId);
		Admob.Instance ().loadInterstitial ();

		#endif
	}

	public void ShowBanner() {
		#if UNITY_EDITOR
		#elif UNITY_ANDROID

		Admob.Instance ().showBannerRelative (AdSize.Banner, AdPosition.BOTTOM_CENTER, 0);

		#endif

	}

	public void RemoveBanner() {
		#if UNITY_EDITOR
		#elif UNITY_ANDROID

		Admob.Instance ().removeAllBanner();

		#endif
	}

	public void ShowInter() {
		#if UNITY_EDITOR
		#elif UNITY_ANDROID

		if (Admob.Instance ().isInterstitialReady()) {
			Admob.Instance ().showInterstitial ();
		}

		#endif
	}
}
