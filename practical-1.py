import requests
import pandas as pd

# Step 1: Connect to API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code) # 200 = success

# Step 2: Parse JSON response
data = response.json()

# Step 3: Convert to DataFrame
df = pd.DataFrame(data)
print(df.head())