import requests
import base64
# import google.generativeai as genai
from google import genai
# from secret_config import GEMINI_API_KEY
from secret import api_key
        

x=input(" enter some input")
print(x)

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=x,
)
print(response.text)

