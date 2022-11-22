import ui

if __name__ == "__main__":
    user = ui.login_user()
    ui.main_menu_loop(user)
    print("Viszlat!")