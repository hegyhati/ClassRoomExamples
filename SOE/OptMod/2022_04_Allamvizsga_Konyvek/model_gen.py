people = {'Kincso', 'Akos', 'Halu'}
courses = {'Optimalizalas', 'Prognyelvek',
           'Webvizualizalas', 'PowerBI', 'Coursera', 'DataAkarmi'}


for p in people:
    for c in courses:
        print(f"var {p}_{c} binary;")

for p in people:
    print(f"s.t. {p}_munkamennyiseg:")
    for c in courses:
        print(f"{p}_{c} + ", end='')
    print("0 = 2;")
