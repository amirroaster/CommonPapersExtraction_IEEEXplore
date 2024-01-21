# Python Script for Extracting Common Papers Based on Keywords

## Overview
This script efficiently identifies and analyzes academic papers that are common across different fields, leveraging specified keywords for the search. Its unique approach involves using cookies obtained from the IEEE Xplore Digital Library. These cookies can be acquired by accessing the developer tools in a web browser while logged into an academic account.

## Requirements
- **Access to IEEE Xplore Digital Library**: A valid academic account is necessary to retrieve the required cookies for the script's operation.

### Initial Setup

```python
import requests, json, hashlib
cookie = "YOUR_COOKIE" # It something like: "fp=38a4e7d2..."
chunkSize = 100
```


We used a segmented approach when searching in IEEE Xplore due to the limitations of the database. Each segment focused on a specific aspect: Index Terms, Abstract, and Document Title.

In the following example, we aim to identify common papers among three groups of keywords. To address the possibility of an invalid cookie, we implemented progress functions. After each page load, we save our progress. This allows us to resume our search from where we left off in case we need to change the cookie later.

```python
# 1
progress = loadProgress('progress.json')

keyword = [
    "semantic",
    "semantics",
    "ontology",
    "ontological",
    "semantic-based",
    "ontology-based",
    "knowledge representation",
    "RDF",
    "OWL",
    "SPARQL",
    "knowledge graph",
    "semantic web",
    "linked data",
    "game system",
    "interaction modeling"]

field = "Index Terms"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 2
progress = loadProgress('progress.json')

keyword = [
    "semantic",
    "semantics",
    "ontology",
    "ontological",
    "semantic-based",
    "ontology-based",
    "knowledge representation",
    "RDF",
    "OWL",
    "SPARQL",
    "knowledge graph",
    "semantic web",
    "linked data",
    "game system",
    "interaction modeling"]

field = "Abstract"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)

# 3
progress = loadProgress('progress.json')

keyword = [
    "semantic",
    "semantics",
    "ontology",
    "ontological",
    "semantic-based",
    "ontology-based",
    "knowledge representation",
    "RDF",
    "OWL",
    "SPARQL",
    "knowledge graph",
    "semantic web",
    "linked data",
    "game system",
    "interaction modeling"]

field = "Document Title"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 4
progress = loadProgress('progress.json')

keyword = [
    "game",
    "gaming",
    "interactive media",
    "virtual reality",
    "digital entertainment"]

field = "Index Terms"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 5
progress = loadProgress('progress.json')

keyword = [
    "game",
    "gaming",
    "interactive media",
    "virtual reality",
    "digital entertainment"]

field = "Abstract"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 6
progress = loadProgress('progress.json')

keyword = [
    "game",
    "gaming",
    "interactive media",
    "virtual reality",
    "digital entertainment"]


field = "Document Title"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)

# 7
progress = loadProgress('progress.json')

keyword = [
    "intelligent agent",
    "NPC",
    "AI",
    "artificial intelligence",
    "multi-agent",
    "player interaction",
    "adaptive gameplay",
    "dynamic content generation"
    ]


field = "Index Terms"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 8
progress = loadProgress('progress.json')

keyword = [
    "intelligent agent",
    "NPC",
    "AI",
    "artificial intelligence",
    "multi-agent",
    "player interaction",
    "adaptive gameplay",
    "dynamic content generation"
    ]

field = "Abstract"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# 9
progress = loadProgress('progress.json')

keyword = [
    "intelligent agent",
    "NPC",
    "AI",
    "artificial intelligence",
    "multi-agent",
    "player interaction",
    "adaptive gameplay",
    "dynamic content generation"
    ]

field = "Document Title"

queryText = makeQueryText(keyword, field)
totalRecords = getTotalRecords(cookie, queryText)

getArticleIds(queryText, totalRecords, progress)


# Common ones?

keyword = [
    "semantic",
    "semantics",
    "ontology",
    "ontological",
    "semantic-based",
    "ontology-based",
    "knowledge representation",
    "RDF",
    "OWL",
    "SPARQL",
    "knowledge graph",
    "semantic web",
    "linked data",
    "game system",
    "interaction modeling"]

field = "Index Terms"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g1_1 = set(progress.get(queryKey, {}).get('articleNumbers', []))


field = "Abstract"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g1_2 = set(progress.get(queryKey, {}).get('articleNumbers', []))

field = "Document Title"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g1_3 = set(progress.get(queryKey, {}).get('articleNumbers', []))

print (f"\nSize of articleNumbers_g1_1: {len(articleNumbers_g1_1)}")
print (f"Size of articleNumbers_g1_2: {len(articleNumbers_g1_2)}")
print (f"Size of articleNumbers_g1_3: {len(articleNumbers_g1_3)}")


articleNumbers_g1 = articleNumbers_g1_1 | articleNumbers_g1_2 | articleNumbers_g1_3

print (f"Size of articleNumbers_g1: {len(articleNumbers_g1)}")

keyword = [
    "game",
    "gaming",
    "interactive media",
    "virtual reality",
    "digital entertainment"]

field = "Index Terms"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g2_1 = set(progress.get(queryKey, {}).get('articleNumbers', []))


field = "Abstract"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g2_2 = set(progress.get(queryKey, {}).get('articleNumbers', []))

field = "Document Title"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g2_3 = set(progress.get(queryKey, {}).get('articleNumbers', []))

print (f"\nSize of articleNumbers_g2_1: {len(articleNumbers_g2_1)}")
print (f"Size of articleNumbers_g2_2: {len(articleNumbers_g2_2)}")
print (f"Size of articleNumbers_g2_3: {len(articleNumbers_g2_3)}")


articleNumbers_g2 = articleNumbers_g2_1 | articleNumbers_g2_2 | articleNumbers_g2_3

print (f"Size of articleNumbers_g2: {len(articleNumbers_g2)}")


keyword = [
    "intelligent agent",
    "NPC",
    "AI",
    "artificial intelligence",
    "multi-agent",
    "player interaction",
    "adaptive gameplay",
    "dynamic content generation"
    ]

field = "Index Terms"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g3_1 = set(progress.get(queryKey, {}).get('articleNumbers', []))


field = "Abstract"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g3_2 = set(progress.get(queryKey, {}).get('articleNumbers', []))

field = "Document Title"
queryText = makeQueryText(keyword, field)
queryKey = hashString(queryText)
print(f"queryKey: {queryKey}")
articleNumbers_g3_3 = set(progress.get(queryKey, {}).get('articleNumbers', []))

print (f"\nSize of articleNumbers_g3_1: {len(articleNumbers_g3_1)}")
print (f"Size of articleNumbers_g3_2: {len(articleNumbers_g3_2)}")
print (f"Size of articleNumbers_g3_3: {len(articleNumbers_g3_3)}")


articleNumbers_g3 = articleNumbers_g3_1 | articleNumbers_g3_2 | articleNumbers_g3_3

print (f"Size of articleNumbers_g3: {len(articleNumbers_g3)}")




articleNumbers = articleNumbers_g1 & articleNumbers_g2 & articleNumbers_g3
print (f"\nSize of articleNumbers: {len(articleNumbers)}")


