import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI

os.environ["OPENAI_API_KEY"] = ''

# reader = SimpleDirectoryReader(
#     input_dir="./data/10k",
#     required_exts=[".pdf"])

# documents = reader.load_data()

lyft_docs = SimpleDirectoryReader(
    input_files=["./data/10k/lyft_2021.pdf"]
).load_data()

index = VectorStoreIndex.from_documents(lyft_docs)
query_engine = index.as_query_engine()
response = query_engine.query("What is this document about?")