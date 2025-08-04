import os
import nest_asyncio
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex

from llama_index.core.node_parser import MarkdownNodeParser
from config import LLAMA_CLOUD_API_KEY, OCR_LANGUAGE

nest_asyncio.apply()
os.environ["LLAMA_CLOUD_API_KEY"] = LLAMA_CLOUD_API_KEY

async def parse_pdf(file_path: str):
    parser = LlamaParse(language=OCR_LANGUAGE)
    documents = await parser.aload_data(file_path)

    node_parser = MarkdownNodeParser()
    nodes = node_parser.get_nodes_from_documents(documents)

    index = VectorStoreIndex(nodes)
    return index
