people = [
    {
        "name": "Adam",
        "apple": 4
    },
    {
        "name": "Balazs",
        "apple": 23
    },
    {
        "name": "Erik",
        "apple": 0
    },
    {
        "name": "Gergo",
        "apple": 15
    },
    {
        "name": "Mate",
        "apple": 3
    }
]

people_with_appletrees = [person 
                          for person in people 
                          if person["apple"] >= 10 ]


my_numbers = [1,2,43,5,3,2,2342,32,2,4]

parity_of_my_numbers = [ number % 2 for number in my_numbers ]