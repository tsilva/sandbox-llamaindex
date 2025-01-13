from dotenv import load_dotenv
load_dotenv()

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("In which letter does this phrase appear: 'I write a few lines in haste to say that I am safe'?")
print(response)