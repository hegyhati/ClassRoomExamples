girl_names = [
    "Emma", "Olivia", "Ava", "Sophia", "Isabella",
    "Mia", "Amelia", "Harper", "Evelyn", "Abigail",
    "Emily", "Ella", "Elizabeth", "Camila", "Luna",
    "Sofia", "Avery", "Mila", "Aria", "Scarlett",
    "Penelope", "Layla", "Chloe", "Victoria", "Madison",
    "Eleanor", "Grace", "Nora", "Riley", "Zoey",
    "Hannah", "Hazel", "Lily", "Ellie", "Violet",
    "Lillian", "Zoe", "Stella", "Aurora", "Natalie",
    "Emilia", "Everly", "Leah", "Aubrey", "Willow",
    "Addison", "Lucy", "Audrey", "Bella", "Nova",
    "Brooklyn", "Paisley", "Savannah", "Claire", "Skylar",
    "Isla", "Genesis", "Naomi", "Elena", "Caroline",
    "Eliana", "Anna", "Maya", "Valentina", "Ruby",
    "Kennedy", "Ivy", "Ariana", "Aaliyah", "Cora",
]

boy_names = [
    "Liam", "Noah", "Oliver", "Elijah", "James",
    "William", "Benjamin", "Lucas", "Henry", "Theodore",
    "Jack", "Levi", "Alexander", "Jackson", "Mateo",
    "Daniel", "Michael", "Mason", "Sebastian", "Ethan",
    "Logan", "Owen", "Samuel", "Jacob", "Asher",
    "Aiden", "John", "Joseph", "Wyatt", "David",
    "Leo", "Luke", "Julian", "Hudson", "Grayson",
    "Matthew", "Ezra", "Gabriel", "Carter", "Isaac",
    "Jayden", "Luca", "Anthony", "Dylan", "Lincoln",
    "Thomas", "Maverick", "Elias", "Josiah", "Charles",
    "Caleb", "Christopher", "Ezekiel", "Miles", "Jaxon",
    "Isaiah", "Andrew", "Joshua", "Nathan", "Nolan",
    "Adrian", "Cameron", "Santiago", "Eli", "Aaron",
    "Ryan", "Angel", "Cooper", "Waylon", "Easton",
]

from random import randint, choice, sample

def generate_random_input(girl_count: int, boy_count: int, average_girl_list_length:int, average_boy_list_length:int):
    girls = sample(girl_names, girl_count)
    boys = sample(boy_names, boy_count)
    return {
        "girls" : {
            girl : sample(boys, randint(average_girl_list_length * 2 // 3, max(boy_count, average_girl_list_length * 4 // 3)))
            for girl in girls
        },
        "boys" : {
            boy : sample(girls, randint(average_boy_list_length * 2 // 3, max(girl_count, average_boy_list_length * 4 // 3)))
            for boy in boys
        }
    }


def export_to_dot(filename, example):
    with open(filename, "w") as f:
        f.write("graph G {\n")
        f.write("  rankdir=LR;\n")
        f.write("  node [shape=circle];\n")
        
        for girl in example["girls"]:
            f.write(f'  "{girl}" [color=pink];\n')
        for boy in example["boys"]:
            f.write(f'  "{boy}" [color=blue];\n')
        
        for girl, boys in example["girls"].items():
            for boy in boys:
                f.write(f'  "{girl}" -- "{boy}";\n')
        f.write("}\n")

def export_to_simple_text(filename, example):
    with open(filename, "w") as f:
        f.write("GIRLS:\n")
        for girl, boys in example["girls"].items():
            f.write(girl + " " + " ".join(boys) + " END\n")
        f.write("BOYS:\n")
        for boy, girls in example["boys"].items():
            f.write(boy + " " + " ".join(girls) + " END\n")
        f.write("END\n\n")

    
# export_to_dot("5_5_2_3.dot", generate_random_input(5,5,2,3))
# export_to_dot("25_25_5_8.dot", generate_random_input(25,25,5,8))

export_to_simple_text("test_small.txt", generate_random_input(8,10,3,4))