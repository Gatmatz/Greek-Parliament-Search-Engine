from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
from preprocess.preprocessing import preprocess_text


def perform_query(search_term):
    indexer_directory = "../backbone/inverse_index"
    ix = open_dir(indexer_directory)

    # Open the index searcher
    s = ix.searcher(weighting=scoring.TF_IDF())

    query_string = preprocess_text(search_term)

    # Create a query parser and parse the query
    query_parser = QueryParser("speech", ix.schema)
    query = query_parser.parse(query_string)

    # Perform the search
    results = s.search(query, limit=100)

    return results







