import os
from dotenv import load_dotenv

load_dotenv()  

LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OCR_LANGUAGE = "tr"
