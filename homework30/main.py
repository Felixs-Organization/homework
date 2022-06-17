import requests # Import requests, if it errors out run pip install requests --user
import os # Import os for file handling
import re # Import re for regular expressions


url = "https://www.nckb.com/gallery-stone-tiles/" # Set the url to the website we want to find images from


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:98.0) Gecko/20100101 Firefox/98.0"
}


response = requests.get(url=url, headers=header)
responsetext = response.text # Get the text from the response


print("sucess" if response.status_code == 200 else "failed")

regex = '<a .*?<div class="envira-lazy".*? <img loading="lazy".*? src="(.*?)".*?</a>' # Set the regex to find the images # WE SUSPECT AN ISSUE WITH THIS REGEX


matches = re.findall(regex, responsetext, re.S) # Find all the matches in the text
if matches != []:
    print("This script found the following images in the URL %s" % url)
    print(matches)
else:
    print("No images found in the URL %s" % url)


with open('site.html', 'w', encoding='UTF-8') as file:
    file.write(responsetext) # Write the text to a file
