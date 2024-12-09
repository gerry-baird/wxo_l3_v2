from fastapi import APIRouter, HTTPException, Request
from starlette import status
from pymilvus import MilvusClient
from pymilvus import model

offer_router = APIRouter()

client = MilvusClient("milvus_demo.db")

if client.has_collection(collection_name="offers_collection"):
    client.drop_collection(collection_name="offers_collection")
client.create_collection(
    collection_name="offers_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

# This will download a small embedding model "paraphrase-albert-small-v2" (~50MB).
embedding_fn = model.DefaultEmbeddingFunction()

# Text strings to search from.
docs = [
    "New travel insurance customers can receive four complimentary passes to airport lounges when they upgrade their medical cover.",
    "Customers renewing their vehicle insurance will receive free breakdown cover.",
    "Customers renewing their travel insurance are eligible for a 5% discount.",
    "We are currently offering discounted gym memberships for customers renewing their health insurance"
    "We are offering free retirement planning consultations for all existing travel insurance customers aged over 30 with a qualified financial planner."
]

vectors = embedding_fn.encode_documents(docs)

data = [
    {"id": i, "vector": vectors[i], "text": docs[i], "subject": "special offers"}
    for i in range(len(vectors))
]
res = client.insert(collection_name="offers_collection", data=data)

def run_search(query, metadata):
    query_vectors = embedding_fn.encode_queries([query])

    res = client.search(
        collection_name="offers_collection",  # target collection
        data=query_vectors,  # query vectors
        limit=5,  # number of returned entities
        output_fields=["text", "subject"],  # specifies fields to be returned
    )

    output_results = []
    for milvus_result in res:
        for doc in milvus_result:
            try:
                entity = doc["entity"]
                output_result = {
                    "title": "Offers",
                    "body": entity["text"]
                }
            except AttributeError as e:
                return f'Malformed search result: {milvus_result}', 500
            except Exception as e:
                return f'Unexpected error for: {milvus_result}.  Error: {e}', 500

            output_results.append(output_result)

    return {"search_results": output_results}
@offer_router.post("/offers")
async def search_offers(request: Request) :
    request = await request.json()
    query = request["query"]
    return run_search(query, None)