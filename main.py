import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.organization = os.getenv('ORG')
openai.api_key = os.getenv('API_KEY')

prompt = 'Make me a complex presentation in language: Croatian. The required number of slides is: 2. The theme is: Prvi svjetski rat.  Presentation should not have a lot of text on one slide. Give me a presentation in this format strictly: { "Slide number": {"title": "Title", "text": "Slide text", "prompt": "Prompt I can feed to image generation" }, ...}'
result = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=1000,
  temperature=1
)

print(json.loads(result.choices[0].text)["Slide 1"]["title"])
