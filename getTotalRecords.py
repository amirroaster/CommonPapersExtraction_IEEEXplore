def getTotalRecords(cookie, queryText):
    """
    Retrieves the total number of records for a given query from the IEEE Xplore Digital Library.

    This function sends a POST request to the IEEE Xplore search API. It uses the provided cookie
    for authentication and sends the query text as part of the request body. The function is designed
    to fetch the total number of records that match the query criteria.

    Parameters:
    cookie (str): A string containing the session cookie for authenticating with the IEEE Xplore API.
    queryText (str): The text query for which the total number of matching records is to be retrieved.

    Returns:
    int: The total number of records found for the query, or an error message if the request fails.

    The function prints and returns an error message if the HTTP request fails or if the response status
    code is not 200 (OK). It uses the 'totalRecords' field in the JSON response to determine the number
    of records.
    """
    print(f"\nget total records...")
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
        "returnFacets": []
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json().get('totalRecords')
    else:
        error_message = f"Error: {response.status_code} on getting total records"
        print(error_message)
        return error_message
