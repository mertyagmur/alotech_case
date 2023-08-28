from google.cloud import bigquery
from flask import jsonify

# Initialize the BigQuery client
bq_client = bigquery.Client()

def get_tech_news_titles(request):
    """
    Google Cloud Function to fetch tech news titles from the bbc_news dataset.
    :param request: HTTP request.
    :return: JSON object containing fetched news titles.
    """
    
    # Construct the SQL query
    sql_query = """
    SELECT title
    FROM `bigquery-public-data.bbc_news.fulltext`
    WHERE category = "tech"
    LIMIT 50
    """

    # Execute the query
    query_job = bq_client.query(sql_query)
    results = [row.title for row in query_job]

    # Create a list of objects with "title" key
    titles_list = [{"title": title} for title in results]

    return jsonify(titles_list)