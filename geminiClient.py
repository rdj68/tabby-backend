import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

model = None

# Function to initialize gemini model
def init_gemini():
  global model
  
  if model is not None:
      return 
  GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
  genai.configure(api_key=GOOGLE_API_KEY)

  # Set up the model
  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
  }


  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]
  model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

# Function to prompt gemini model and return response
async def prompt_gemini(promptParts):
  global model
  if model is None:
    init_gemini()
  
  response = await model.generate_content_async(promptParts)
  return response