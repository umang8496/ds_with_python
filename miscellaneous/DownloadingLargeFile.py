##Downloading Large Files
##But not for Video Files

import requests

file_url = input("Enter the File URL : ")

web_content = requests.get(file_url, stream = True)

with open("doc.txt","wb") as file:
     for chunk in web_content.iter_content(chunk_size = 1024):
          if chunk:
               file.write(chunk)

print("Download Completed")
