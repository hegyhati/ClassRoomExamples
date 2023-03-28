DC_universe = {
    "superhero" : [
        "Batman",
        "Superman",
        "Wonderwoman",
        "Canary",
        "Raven"
    ],
    "villain" : [
        "Joker",
        "Luthor",
        "Tigress",
        "Kiteman",
        "Boy wonder"
    ]
}

def print_authors(book):
    for author in book["authors"]:
        print(f" - {author['firstname']} {author['lastname']}")


library = [
    {
        "title" : "OpenGL superbible",
        "authors" : [
            {
                "firstname" : "Richard",
                "middlename" : "S.",
                "lastname" : "Wright",
                "suffix" : "Jr."
            },
            {
                "firstname" : "Michael",
                "lastname" : "Sweet"
            }
        ],
        "pages" : 714,
        "language" : "en",
        "color": False
    },
    {
        "title" : "Babaház",
        "authors" : [
            {
                "firstname" : "Henrik",
                "lastname" : "Ibsen"
            }
        ],
        "language" : "hu",
        "color" : False
    }
]

for book in library:
    print(book['title'])
    print_authors(book)