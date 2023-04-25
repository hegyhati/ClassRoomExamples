with open("data.csv") as data:
    last_items = [ line.split(',')[-1].strip() for line in data ]

good_items = [ float(item) for item in last_items if item != '#DIV/0!' ]

print(good_items)