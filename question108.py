import requests

# Fetch data from a public API
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

# Print part of the JSON response
print("First post title:", data[0]['title'])
