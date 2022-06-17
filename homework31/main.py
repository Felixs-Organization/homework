import requests Import requests, if it errors out run pip install requests --user
import os Import os for file handling
import re Import re for regular expressions


urls = [
    "https://www.nckb.com/atherton-project-1/",
"https://www.nckb.com/atherton-project-2/",
"https://www.nckb.com/atherton-project-3/",
"https://www.nckb.com/atherton-project-4/",
"https://www.nckb.com/atherton-project-5/",
"https://www.nckb.com/atherton-project-6/",
"https://www.nckb.com/atherton-project-7/",
"https://www.nckb.com/atherton-project-8/",
"https://www.nckb.com/kentfield-ca/",
"https://www.nckb.com/misc-projects/",
"https://www.nckb.com/orinda-ca/",
"https://www.nckb.com/gallery-portola-valley-ca/",
"https://www.nckb.com/san-francisco-ca/"
]


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:98.0) Gecko/20100101 Firefox/98.0"
}



i2 = 1
for url in urls:
    if not os.path.exists("D:/Python/homework31/images{}/".format(str(i2))):
        os.makedirs("D:/Python/images{}/".format(str(i2)))
    response = requests.get(url=url, headers=header)
    responsetext = response.text Get the text from the response


    print("Sucessfully got %s" % url if response.status_code == 200 else "failed")

    regex = '<div id=".*?".*?<div class="envira-lazy" .*?<img loading="lazy".*?src="(.*?)".*?</div>.*?</div>' Set the regex to find the images WE SUSPECT AN ISSUE WITH THIS REGEX




    matches = re.findall(regex, responsetext, re.S) Find all the matches in the text
    if matches != []:
        print("This script found the following images in the URL" % url)
        print(matches)
    else:
        print("No images found in the URL %s" % url)

    if matches != []:
        i = 1
        for source in matches:
            response = requests.get(source, headers=header)
            data = response.content
            filename = "./images{0}/image{1}.jpg".format(str(i2), str(i))
            with open(filename, "wb") as f:
                f.write(data)
                print("Downloaded image %d" % i)
                print("Saved image as images/image%d.jpg" % i)
                print("downloaded from %s" % source)
            i += 1


print("Finished!")