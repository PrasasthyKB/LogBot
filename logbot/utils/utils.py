"""Utility functions to help with coding aspects of the project
"""
def build_logfile_response(query, response, timestamp_sort, doc):
    """build response body for logFile Collection

    Args:
        query (string): _description_
        response (string): _description_
        timestamp_sort (string): _description_
        doc (dict): _description_

    Returns:
        dict: dictionary containing the document details
    """
    return { 
        'chathistory': {'query':query,
        'response':response,
        'timestamp' :timestamp_sort
            },
        'docdetails':{
            'document_id': doc['document_id'],
            'document_name': doc['document_name'],
            'doc_summaries': doc['document_summary'],
            'doc_tag': doc['document_tag'],
            'doc_timestamp' : doc['timestamp'] }
    } 
