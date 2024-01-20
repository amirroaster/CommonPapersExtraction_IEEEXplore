def getArticleIds(queryText, totalRecords, progress):
    """
    Retrieves article IDs based on a query, updates progress, and saves it.

    Parameters:
    queryText (str): The query text used to search for articles.
    totalRecords (int): The total number of records matching the query.
    progress (dict): A dictionary containing progress data.

    This function retrieves article IDs for a given query and updates progress data accordingly.
    It calls the search endpoint for multiple pages, adds new article IDs to the progress data,
    and saves the updated progress to a file.
    """  
    print(f"\ngetArticleIds for {totalRecords} records...")
    
    queryKey = hashString(queryText)
    print(f"queryKey: {queryKey}")
    articleNumbers = set(progress.get(queryKey, {}).get('articleNumbers', []))

    startPage = progress.get(queryKey, {}).get('lastPage', 0)
  


    if not articleNumbers:
        print("\nThere is no article found in the 'progress.json' related to the query...")
    else:
        print(f"\nThere are some articles found in the 'progress.json' related to the query. The articles from the page '1' to '{startPage}' are already added!")

    startPage= startPage+1
    lastPage = (totalRecords - 1) // chunkSize + 1

    if startPage > lastPage: print("No new articles to add.")

    else:

        print(f"Let's call the search endpoint for the pages from '{startPage}' to '{lastPage}'...")

        pageNumber = startPage

        for i in range(startPage, lastPage+1, 1):
            pageNumber = i
            startRecord = (pageNumber-1)*chunkSize+1
            endRecord = min(startRecord + chunkSize - 1, totalRecords)

            

            print(f"\nFinding articles '{startRecord}' to '{endRecord}' on the page '{pageNumber}'...")

            result = search(cookie, queryText, pageNumber, lastPage)
        

            if isinstance(result, str):
                print(f"Error encountered: {result}. Stopping further requests.")
                break
            
            else:
            
                currentArticleNumbers = {record["articleNumber"] for record in result.get('records', []) if "articleNumber" in record}
                print(f"\nArticle numbers in this chunk: {currentArticleNumbers}")
                newElements = currentArticleNumbers - articleNumbers

                if newElements:
                    print("There are new articles to add:", newElements)
                    articleNumbers.update(currentArticleNumbers)
                else:
                    print("No new articles to add.")

                articleNumbers.update(currentArticleNumbers)
                progress[queryKey] = {'lastPage': pageNumber, 'articleNumbers': list(articleNumbers)}
                saveProgress('progress.json', progress)

