from llama_index.core import VectorStoreIndex
from llama_index.core import download_loader
from config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def parse_pptx(file_path: str):
    PPTXReader = download_loader("PPTXReader")
    loader = PPTXReader()
    documents = loader.load_data(file_path=file_path)

    index = VectorStoreIndex(documents)
    return index
