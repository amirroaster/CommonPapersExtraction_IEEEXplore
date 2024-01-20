def makeQueryText(keywords, field):
    """
    Generates a query string for searching keywords within a specific field.

    Parameters:
    keywords (list of str): List of keywords to search for.
    field (str): The field in the database to search within.

    Returns:
    str: Formatted query string.

    Constructs a query string by joining keywords with 'OR' and formatting it to search
    within the specified field.
    """  
    queryTerms = ' OR '.join([f'\"{keyword}\"' for keyword in keywords])
    queryString = f"{field}: ({queryTerms})"
    print(f"\nqueryText: {queryString}")
    return queryString


def hashString(input_string):
    """
    Computes the SHA-256 hash of an input string.

    Parameters:
    input_string (str): The string to be hashed.

    Returns:
    str: The hexadecimal representation of the SHA-256 hash.

    This function calculates the SHA-256 hash of the input string and returns it as a
    hexadecimal string.
    """  
    sha256 = hashlib.sha256()
    
    sha256.update(input_string.encode('utf-8'))

    return sha256.hexdigest()


def saveProgress(filename, progress_data):
    """
    Saves progress data to a JSON file.

    Parameters:
    filename (str): The name of the JSON file to save the data to.
    progress_data (dict): The progress data to be saved.

    This function attempts to save the provided progress_data dictionary to the specified JSON file.
    If successful, it prints a confirmation message; otherwise, it prints an error message.
    """  
    try:
        with open(filename, 'w') as file:
            json.dump(progress_data, file)
        print(f"Progress saved to {filename}")
    except Exception as e:
        print(f"Error saving progress: {e}")


def loadProgress(filename):
    """
    Loads progress data from a JSON file or creates a new one if not found.

    Parameters:
    filename (str): The name of the JSON file to load progress data from or create.

    Returns:
    dict: A dictionary containing the loaded progress data or an empty dictionary if not found.

    This function attempts to load progress data from the specified JSON file. If the file exists,
    it returns the loaded data. If the file doesn't exist, it creates a new one and returns an empty dictionary.
    Any other exceptions during the process are handled with error messages.
    """  
    try:
        with open(filename, 'r') as file:
            progress = json.load(file)
            print(f"Progress loaded from {filename}")
            return progress
    except FileNotFoundError:
        print(f"No existing progress file found ({filename}). Creating a new one.")
        with open(filename, 'w') as file:
            json.dump({}, file)  # Create a new file with an empty JSON object
        return {}
    except Exception as e:
        print(f"Error loading progress: {e}")
        return {}
