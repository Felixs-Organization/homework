import requests
import sys
import os
import json

# Check if the correct amount of arguments are passed
if len(sys.argv) != 4:
    print("Usage: python3 main.py <url> <filename> <user-agent>")
    sys.exit(1)

url = sys.argv[1] # Get the url from the command line
port = url.split(':')[-1]
filename = sys.argv[2]
useragent = sys.argv[3]

# Append http:// to the url if it doesn't exist
if url[:7] != "http://":
    url = "http://" + url
# Check if the file exists
if os.path.isfile(filename):
    print("Filename passed in exists, please check the filename")
    sys.exit(1)

# Check the status code
status_code = requests.get(url).status_code
if status_code != 200:
    print("Status code is not 200, please check the url")
    sys.exit(1)
print(f"URL: {url}\tFilename: {filename}")
proxy = {
    "http": "http://localhost:8080"
}

# Download the file
with open(filename, "w") as f:
    response = requests.get(url, headers={"User-Agent": useragent}, proxies=proxy)
    if response.content_type == "application/json":
        json_data = response.json()
        f.write(json.dumps(json_data))
    else: 
        f.write(response.text)
    print(f"File wrote to {filename}")


sys.exit(0)