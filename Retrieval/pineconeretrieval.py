def pineconeretrieval(vectordb, query, search_type):
    return vectordb.as_retriever(search_type = search_type)