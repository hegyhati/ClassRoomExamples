import json


def collect_tags(articles):
    return { tag for article in articles for tag in article["tags"] }

def get_ids_by_text(articles, text):
    return [ article["id"] for article in articles
            if text.lower() in article["title"].lower() or text.lower() in article["content"].lower() ]

def get_ids_by_tag(articles, tag):
    return [ article["id"] for article in articles if tag in article["tags"] ] 
    
def get_ids_by_dates(articles, first, last):
    return [ article["id"] for article in articles if first <= article["date"] <= last ]

def get_article_by_id(articles, id):
    for article in articles:
        if article["id"] == id:
            return article
        

def ui_search_by_text(articles):
    text = input("Keresendő kifejezés: ")   
    return get_ids_by_text(articles, text)

def ui_search_by_tag(articles):
    tags = collect_tags(articles)
    print(f"Címkék: {', '.join(tags)}")
    while True:
        tag = input("Választott címke (vagy \"back\" a visszalépéshez): ")
        if tag == "back": return
        elif tag in tags: return get_ids_by_tag(articles, tag)
        else: print("Nincs ilyen címke!")

def ui_search_by_dates(articles):
    first = input("Kérem a kezdődátumot (YYY-MM-DD): ")
    last = input("Kérem a végdátumot (YYY-MM-DD): ")
    return get_ids_by_dates(articles, first, last)

ui_get_ids = {
    1: ui_search_by_text,
    2: ui_search_by_tag,
    3: ui_search_by_dates
}

def show_titles(articles, ids):
    for article in articles:
        if article["id"] in ids:
            print(f"{article['id']}: {article['title']}")

def ui_select_article(articles, ids):
    if len(ids) == 0 : 
        print("Nincs találat")
        return 0
    show_titles(articles, ids)
    while True:
        selected = int(input("Kérem az ID-t (vagy 0: vissza a menübe): "))
        if selected == 0 or selected in ids: return selected
        else: print("Nincs ilyen ID a találatok között!")

def show_article(articles, id):
    article = get_article_by_id(articles, id)
    print(f"""
        # {article["title"]}
        
        *Megjelent: {article["date"].replace("-",".")}.*    
        
        {article["content"]}  
        
        Címkék: {". ".join(article["tags"])}""")
    

def menu():
    return int(input("""
        Válasszon menüpontot:
        1: Keresés szöveggel
        2: Szűrés címkére
        3: Szűrés időintervallumra
        0: Kilépés
        Választás: """))



if __name__ == "__main__":
    with open("cikkek.json") as f:
        articles = json.load(f)

    print(f"{len(articles)} cikk sikeresen betöltve")

    while True:
        selection = menu()
        if selection == 0 : exit()
        ids = ui_get_ids[selection](articles)
        selected = ui_select_article(articles, ids)
        if selected != None and selected != 0:
            show_article(articles, selected)  