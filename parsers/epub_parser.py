from llama_index.core import VectorStoreIndex
from llama_index.core import download_loader
from config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def parse_epub(file_path: str):
    EpubReader = download_loader("EpubReader")
    loader = EpubReader()
    documents = loader.load_data(file_path=file_path)

    index = VectorStoreIndex(documents)
    return index
