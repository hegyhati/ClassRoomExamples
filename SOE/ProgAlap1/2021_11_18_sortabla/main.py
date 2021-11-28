from typing import List
import backend

def register_new_run() -> None:
    date = input("Mikor volt a futas? (yyyy.mm.dd.) ")
    #todo lecsekkolni
    runners = input("Kik futottak? (vesszovel elvalaszttva) ")
    runners = [ name.strip() for name in runners.split(",") ]
    backend.save_new_run(date, runners)
    print("Uj futas elmentve")


def print_run_count(data:List[dict]):
    print(f"Eddig {len(data)} alkalommal volt futas.")

def print_runner_count_and_list(data:List[dict], print_list = False):
    runners = backend.list_of_runners(data)
    print(f"Eddig osszesen {len(runners)} futo jott el", end="")
    if print_list :
        print(":")
        for runner in runners:
            print(f" - {runner} ({backend.count_runs(data,runner)})")
    else:
        print(".")
    backend.svg_export_runners(data)


def statistics() -> None:
    data=backend.load_data()
    print_run_count(data)
    print_runner_count_and_list(data,True)
    




def menu_select() -> int:
    print()
    print("=============================")
    print("Mit szeretnel csinalni?")
    print(" 1. uj futas felvitele.")
    print(" 2. statisztikak")
    print(" 3. kilepes")
    return int(input()) # todo nem szam bemenet



if __name__ == "__main__":
    while True:
        option = menu_select()
        if option == 3:
            exit()
        elif option == 2:
            statistics()
        elif option == 1:
            register_new_run()
        else:
            print("Rossz szamot adtal meg.")
