from bs4 import BeautifulSoup
import requests

emails = set()

organizations = {
    "BPK" : 78, 
    "EMK" : 83, 
    "LKK" : 35, 
    "FMK" : 335, 
    "ERTI": 329
}

url = "https://www.uni-sopron.hu/organog/list/id/{}/m/1112/page/{}"

for org, id in organizations.items():
    for page in range(1,20):
        print(f"Sraping organization {org} page {page} ...", end="")
        
        website = requests.get(url.format(id,page))
        org_soup = BeautifulSoup(website.content, "html.parser")
        people_div = org_soup.find(id="content-pos")
        linkek = people_div.find_all("a")
        for link in linkek:
            if "mailto" in link["href"]:
                innerHTML = link.decode_contents()
                email = innerHTML.replace("##kukac##", "@")
                emails.add(email)
        
        print("DONE")

with open("soe_emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")