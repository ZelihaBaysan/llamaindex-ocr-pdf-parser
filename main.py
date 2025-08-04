import os
import asyncio
from parsers import pdf_parser, docx_parser, epub_parser, html_parser, md_parser, pptx_parser, txt_parser

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()

async def parse_file(file_path: str):
    ext = get_file_extension(file_path)
    
    if ext == ".pdf":
        return await pdf_parser.parse_pdf(file_path)
    elif ext == ".docx":
        return docx_parser.parse_docx(file_path)
    elif ext == ".epub":
        return epub_parser.parse_epub(file_path)
    elif ext == ".html" or ext == ".htm":
        return html_parser.parse_html(file_path)
    elif ext == ".md":
        return md_parser.parse_md(file_path)
    elif ext == ".pptx":
        return pptx_parser.parse_pptx(file_path)
    elif ext == ".txt":
        return txt_parser.parse_txt(file_path)
    else:
        raise ValueError(f"Desteklenmeyen dosya türü: {ext}")

async def main():
    file_path = "./data/input/sample_scanned.pdf"  # Burayı kendi test dosyanla değiştir
    
    print(f"Parsing dosya: {file_path}")
    index = await parse_file(file_path)

    query_engine = index.as_query_engine()
    response = query_engine.query("Bu belge ne hakkında?")
    print("Soru-Cevap sonucu:", response)

if __name__ == "__main__":
    asyncio.run(main())
