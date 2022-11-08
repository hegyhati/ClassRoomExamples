import backend

def login_user():
    while True:
        username = input("Felhasznalonev: ")
        password = input("Jelszo: ")
        user = backend.is_valid_user(username,password) 
        if user: 
            return user
        else:
            print("Hibas felhasznalonev, jelszo.")

def print_menu(user): # user will be needed later for roles
    print()
    print(" 1. Uj tesiora  felvitele.")
    print(" 2. Meglevo tesiora szerkesztese.")
    print(" 3. Uj felhasznalo felvitele.")
    print(" 4. Jelszomodositas.")
    print(" 5. Kilepes")

def new_password_dialog():
     while True:
        new_password = input("Add meg az uj jelszot: ")
        new_password_confirmation = input("Add meg ujra a jelszot: ")
        if new_password == new_password_confirmation:
            return new_password
        else:
            print("Nem egyezik a ket jelszo, add meg oket ujra.")

def change_password_dialog(user):
    new_password = new_password_dialog()
    backend.update_password(user["username"],new_password)
    print("Jelszo sikeresen modositva.")

def main_menu_loop(user):
    print(f"Szia {user['realname']}!")    
    while True:
        print_menu(user)
        selection = int(input("Mit szeretnel csinalni? "))
        if selection == 5: return
        elif selection == 4:
            change_password_dialog(user)            
        else:
            print("Meg nincs implementalva, gyere vissza kesobb.")
