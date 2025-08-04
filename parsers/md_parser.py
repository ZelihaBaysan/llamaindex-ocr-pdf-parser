from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
from config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def parse_md(file_path: str):
    MarkdownReader = download_loader("MarkdownReader")
    loader = MarkdownReader()
    documents = loader.load_data(file_path=file_path)

    index = VectorStoreIndex(documents)
    return index
