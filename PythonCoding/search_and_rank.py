documents = [
    "Python is great for data analysis",
    "I love writing Python code",
    "Data science uses Python",
    "Cooking recipes are fun"
]

Query = "Python data"


def search_documents(documents, query):
    """
    Search and rank documents based on the query.
    """
    if not documents or not query:
        return []

    query_tokens = query.lower().split() 


    
    