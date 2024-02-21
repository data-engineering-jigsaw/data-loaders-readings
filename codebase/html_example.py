from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.web import SimpleWebPageReader

os.environ["OPENAI_API_KEY"] = ''

documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["http://paulgraham.com/worked.html"]
)
parser = SentenceSplitter(chunk_size=1024)
nodes = parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine = index.as_query_engine()
response = query_engine.query("What is this document about?")
