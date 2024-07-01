import matplotlib.pyplot as plt
import argparse
import json

DATA_FILE = "locations.json"

__DATA = None



def load_data():
    global __DATA
    if not __DATA:
        with open(DATA_FILE, "r") as f:
            __DATA = json.load(f)

def persist_data():
    if __DATA:
        with open(DATA_FILE, "w") as f:
            json.dump(__DATA, f, indent=2)

def get_location_id():
    print("Locations:")
    for location in __DATA:
        print(f" {location['id']}: {location['name']}")
    return input("Selected location ID: ")

def fetch_location(location_id):
    for location in __DATA:
        if location["id"] == location_id:
            return location

def select_product(location):
    print(f"Products at location {location['name']}:")
    for id, product in location["products"].items():
        print(f" - {id}: {product['amount']} {product['name']} ({product['color']})")
    id = input("Select product ID: ")
    return id, location["products"][id]    



 
def edit_action(args):
    if not args.l:
        args.l = get_location_id()
    location = fetch_location(args.l)
    pid, product = select_product(location)
    
    action = int(input("""Select action:
                   1 - Decrease amount
                   2 - Increase amount
                   3 - Move amount to another location
                   4 - Rename product
                   5 - Delete product
                   """))
    match action:
        case 1:
            product["amount"] -= int(input("Amount to decrease: "))
        case 2:
            product["amount"] += int(input("Amount to increase: "))
        case 3:
            amount = int(input("Amount to move: "))
            print("Where to move?")
            destination = fetch_location(get_location_id())
            product["amount"] -= amount
            if pid in destination["products"]:
                destination["products"][pid]["amount"] += amount
            else:
                destination["products"][pid] = product.copy()
                destination["products"][pid]["amount"] = amount
        case 4:
            new_name = input("New name: ") # assuming that renaming is for all locations
            for location in __DATA:
                if pid in location["products"]:
                    location["products"][pid]["name"] = new_name
        case 5:
            del location["products"][pid]




def get_all_pids():
    return {pid for location in __DATA for pid in location["products"]}

def unique_pid():
    return str(max(int(pid) for pid in get_all_pids()) + 1)

def new_product_action():
    while True:
        name = input("Product name: ")
        amount = int(input("Product amount: "))
        color = input("Product color: ")
        while True:
            pid = input("Product ID: ") 
            if pid not in get_all_pids(): # Assuming that new id cannot collide
                break
            print("Product ID already exists")
        if not pid: 
            pid = unique_pid()
        location = fetch_location(get_location_id())
        
        location["products"][pid] = {
            "name": name,
            "amount": amount,
            "color": color
        }
        
        if input("Add another product? (y/n): ") == "n":
            break


def generate_statistics():
    fig,axs = plt.subplots(len(__DATA))
    for i, location in enumerate(__DATA):
        axs[i].bar(
            [product["name"] for product in location["products"].values()],
            [product["amount"] for product in location["products"].values()]
        )
        axs[i].set_title(location["name"])
    fig.tight_layout()
    fig.savefig("statistics.png")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", type=str, help="Location ID")
    parser.add_argument("-n", action="store_true", help="Add new product")
    parser.add_argument("--stats", action="store_true", help="Generate statistics")
    
    return parser.parse_args()


def main():
    args = parse_args()
    load_data()
    
    if args.n: 
        new_product_action()
    elif args.stats:
        generate_statistics()
    else:
        edit_action(args)
        
    persist_data()
    

if __name__ == "__main__":
    main()
    

    """


## EXTRA

Kényelmi funkciók megvalósítása.

A programban legyen lehetőség a mennyiségek csökkentésére a `-m` kapcsoló megadásával. A kapcsoló megadásakor a program várjon egy kötelező `<id>` argumentumot és egy mennyiséget pl: `-10`, `+10`.

A program ekkor írja ki, hogy melyik termék és hogyan változott `Termék 1: 10 -> 20`
"""