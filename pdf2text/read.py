import chromadb

# Initialize Chroma DB client
client = chromadb.PersistentClient(path="./dbset/db2")
collection = client.get_collection(name="my_collection")
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize GPT4All embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="moka-ai/m3e-small",
    model_kwargs={"device": "cuda"}
)

# Get user input
query = """
充电桩有哪些故障信息,包括故障模式即故障名称、故障原因和故障影响以及相关的系统组成
"""

# Convert query to vector representation
query_vector = embeddings.embed_query(query)

# Query Chroma DB with the vector representation
results = collection.query(query_embeddings=query_vector, n_results=500, include=["documents"])

with open('dataset.txt', 'a', encoding='utf-8') as file:
    # 遍历每个结果
    for result in results["documents"]:
        # 遍历当前结果中的每个字符串
        for i in result:
            if type(i) == str:
                file.write("\n" + i.replace("\n", ""))
