from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
from config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def parse_html(file_path: str):
    HTMLReader = download_loader("HTMLReader")
    loader = HTMLReader()
    documents = loader.load_data(file_path=file_path)

    index = VectorStoreIndex(documents)
    return index
