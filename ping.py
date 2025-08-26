import requests
import time

url = "https://google.com"

start_time = time.time()

requests.get(url)

end_time = time.time()

duration = (end_time - start_time) * 1000

print(f"Response from {url} took: {duration} ms")
