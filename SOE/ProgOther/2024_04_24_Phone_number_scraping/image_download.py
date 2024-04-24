import requests

url = "https://www.uni-sopron.hu/images/szemelyek/hegyhati_mate.jpg"

image = requests.get(url)

filename = url.split("/")[-1]

with open(filename, "wb") as f:
    f.write(image.content)

    
