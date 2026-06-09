from memory.vector_store import collection


def retrieve_context(query: str, limit: int = 3):

    results = collection.query(
        query_texts=[query],
        n_results=limit
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)