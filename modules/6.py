from urllib.parse import urlparse

url = "https://www.google.com/search?q=python"

result = urlparse(url)

print("Scheme:", result.scheme)
print("Domain:", result.netloc)
print("Path:", result.path)
print("Query:", result.query)