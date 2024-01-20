def search(cookie, queryText, pageNumber, last_page):
    """
    Performs a search query on IEEE Xplore and retrieves results for a specific page number.

    Parameters:
    cookie (str): Authentication cookie for IEEE Xplore.
    queryText (str): Text to search for in the IEEE Xplore database.
    pageNumber (int): The specific page number to retrieve results from.
    last_page (int): The last page number available for the query.

    Returns:
    dict or str: Search results in JSON format if successful, or an error message if not.

    The function sends a POST request with the search query. It checks if the requested page number
    does not exceed the limit (100). If the request is successful, it returns the JSON response, else
    it returns an error message.
    """
    print(f"\nCalling the search endpoint for the page '{pageNumber}/{last_page}'...")

    if (pageNumber > 100):
        errorMessage = "Error: The max pageNumber could be 100 and nothing more!"
        return errorMessage
    url = "https://ieeexplore.ieee.org/rest/search"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Cookie": cookie
    }
    body = {
        "action": "search",
        "matchBoolean": "true",
        "newsearch": "true",
        "queryText": queryText,
        "highlight": "true",
        "returnType": "SEARCH",
        "matchPubs": "true",
        "pageNumber": pageNumber,
        "rowsPerPage": "100",
        "returnFacets": []
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        print(f"Data fetched successfully for the page '{pageNumber}'.")
        return response.json() 
    else:
        errorMessage = f"Error: {response.status_code} on the page '{pageNumber}'"
        print(errorMessage)
        return errorMessage
