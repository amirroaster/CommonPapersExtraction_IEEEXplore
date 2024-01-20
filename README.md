# Python Script for Extracting Common Papers Based on Keywords

## Overview
This script efficiently identifies and analyzes academic papers that are common across different fields, leveraging specified keywords for the search. Its unique approach involves using cookies obtained from the IEEE Xplore Digital Library. These cookies can be acquired by accessing the developer tools in a web browser while logged into an academic account.

## Requirements
- **Access to IEEE Xplore Digital Library**: A valid academic account is necessary to retrieve the required cookies for the script's operation.

### Initial Setup

```python
import requests, json, hashlib
cookie = "fp=38a4e7d2a761bb0feea68842159ecfd2; s_ecid=MCMID%7C63806046576518741164168996566958498187; ..."
chunkSize = 100
