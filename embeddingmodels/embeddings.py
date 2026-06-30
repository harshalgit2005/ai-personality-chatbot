# Import HuggingFaceEmbeddings from LangChain.
# This allows us to use embedding models from Hugging Face.
from langchain_huggingface import HuggingFaceEmbeddings


# Load the embedding model.
#
# all-MiniLM-L6-v2:
# - Small (~80 MB)
# - Fast
# - Runs on CPU
# - Produces 384-dimensional vectors
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# embed_query() → Used for the user's search question.
#
# Example:
# User asks a question and we convert it into a vector.
query_vector = embeddings.embed_query(
    "you are going to learn gen ai"
)


# Print the query embedding vector.
print("Query Vector:")
print(query_vector)


# Print vector dimension.
print("\nQuery Vector Length:", len(query_vector))


# ------------------------------------------------------------


# embed_documents() → Used for documents/chunks that will be
# stored in a vector database.
#
# Example documents that might come from:
# - PDFs
# - Websites
# - Text files
# - Database records
documents = [
    "Generative AI is a branch of artificial intelligence.",
    "Python is one of the most popular programming languages.",
    "Machine learning is a subset of artificial intelligence."
]


# Convert all documents into embedding vectors.
document_vectors = embeddings.embed_documents(documents)


# Print total number of document vectors generated.
print("\nNumber of Document Vectors:", len(document_vectors))


# Print dimension of the first document vector.
print("Document Vector Length:", len(document_vectors[0]))


# Print first 10 values of the first document vector.
print("\nFirst Document Vector (First 10 Values):")
print(document_vectors[0][:10])