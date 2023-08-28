# Tech News Titles Fetcher

This is a simple Google Cloud Function that is done as the AloTech Junior Developer Challenge which fetches tech news titles from a BigQuery dataset and returns them in JSON format. The function is written in Python and can be triggered via an HTTP request.

## Setup

   - Open the Google Cloud Console.
   - Create a new Cloud Function.
   - Name: Choose a name for your function.
   - Runtime: Choose the appropriate Python version.
   - Entry point: `get_tech_news_titles`.
   - Deploy the function using the provided Python code.

## Trigger 
The following trigger URL demonstrates the function:
https://us-central1-alotech-case.cloudfunctions.net/get_tech_titles
