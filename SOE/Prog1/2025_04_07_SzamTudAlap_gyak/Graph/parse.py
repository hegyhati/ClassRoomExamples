import json


def parse_to_adjacency_list(filename):
    with open(filename) as f:
        data = json.load(f)

    names = list(data.keys())
    
    # listas = []
    # for idx,name in enumerate(names):
    #     neighbors = []
    #     for neighbor in data[name]:
    #         neighbors.append(names.index(neighbor))
    #     listas.append(neighbors)
    # print(listas)

    return [
        [ names.index(neighbor) for neighbor in data[name] ]
        for idx,name in enumerate(names)
    ]

def parse_to_adjacency_matrix(filename):
    with open(filename) as f:
        data = json.load(f)

    names = list(data.keys())
    return [
        [True if name2 in data[name] else False for name2 in names]
        for name in names
    ]


if __name__ == "__main__":
    print(parse_to_adjacency_list("gain2024.json"))
    print(parse_to_adjacency_matrix("gain2024.json"))