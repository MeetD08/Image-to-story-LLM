from dotenv import load_dotenv, find_dotenv
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain_core.prompts import PromptTemplate
import requests
import os
from huggingface_hub import InferenceClient
import google.generativeai as genai


HUGGINGFACE_TOKEN = os.getenv("access_key")

genai.configure(api_key="")
load_dotenv(find_dotenv())
model = genai.GenerativeModel("gemini-1.5-flash")

def image2text(url):
    image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-large")
    text = image_to_text(url)[0]["generated_text"]

    print(text)
    return text

image2text("bottle1.png")

def generate_story(scenerio):
    prompt = f"""
    You are a story writer. You are given a scenario and you need to write a story about it.
    Scenario: {scenerio}
    Story:
    """
    
    response = model.generate_content(prompt)
    story = response.text
    print(story)
    return story


def text2speech(story):
    api_url = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    payload = {
        "inputs": story
    }

    response = requests.post(api_url,headers=headers,json=payload)
    with open("story.flac","wb") as f :
        f.write(response.content)


scenerio = image2text("bottle1.png")
story = generate_story(scenerio)
text2speech(story)
