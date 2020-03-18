##Downloading Images from Internet
##https://www.facebook.com/photo.php?fbid=1344930685620351&l=18da8752e3

import requests
image_url = input("Enter the image url for downloading : ")
file_name = input("Enter the name for the image : ")

web_content = requests.get(image_url)

with open(file_name,"wb") as file:
     file.write(web_content.content)

print("Image Downloaded")
