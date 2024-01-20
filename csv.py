def fetch_ieee_csv(cookie, documentIds):
    # Fetches CSV data from IEEE Xplore based on provided document IDs using a POST request.
    print(f"fetch_ieee_csv...")
    url = "https://ieeexplore.ieee.org/rest/search/export-csv"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Cookie": cookie
    }
    body = {
        "action": "search",
        "matchBoolean": "true",
        "newsearch": "true",
        "highlight": "true",
        "returnFacets": [],
        "returnType": "SEARCH",
        "matchPubs": "true",
        "documentIds":  list(documentIds)
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.content
    else:
        return f"Error: {response.status_code}"


def save_csv_data(csv_data, filename):
    # Saves CSV data to a specified filename. Checks for non-empty data and ensures the filename ends with .csv.
  
    # Check if the data is not empty
    if csv_data:
        # Ensure the filename ends with .csv
        if not filename.endswith('.csv'):
            filename += '.csv'

        # Write the data to the file
        with open(filename, 'wb') as file:
            file.write(csv_data)
        print(f"CSV data saved to {filename}")
    else:
        print("No data to save.")

csv_data = fetch_ieee_csv(cookie, articleNumbers)
filename = "ieee_data"
save_csv_data(csv_data, filename)
