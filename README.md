📸 Image-to-Story LLM

This project takes an image and turns it into an audio story in three steps:
	1.	Image to Text – The image is captioned using the BLIP image-to-text model from Hugging Face.
	2.	Text to Story – The caption is expanded into a creative story using Google’s Gemini 1.5 Flash model.
	3.	Story to Speech – The story is converted into speech using Hugging Face’s ESPnet VITS model.

⸻

🚀 Features
	•	Fully automated: Just give an image, and it returns an audio story.
	•	Multi-model pipeline:
	•	Salesforce/blip-image-captioning-large for image captioning
	•	gemini-1.5-flash for story generation
	•	espnet/kan-bayashi_ljspeech_vits for text-to-speech
	•	Environment variable support via .env file for secure API keys.

