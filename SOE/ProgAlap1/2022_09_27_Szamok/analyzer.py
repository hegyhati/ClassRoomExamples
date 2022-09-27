with open("test.txt") as f:
    data = f.readline().strip()

data = data.split(',')

data = [ int(x) for x in data ]

# print(data)

statistics = []

statistics.append( ("Count", len(data)))
statistics.append( ("Maximum", max(data)))
statistics.append( ("Minimum", min(data)))
statistics.append( ("Average", sum(data) / len(data)))

count = [0] *101

for item in data:
    count[item] += 1

statistics.append(("Most common element", count.index(max(count))))

print(statistics)

maxlen = 0
for (text,number) in statistics:
    if len(text) > maxlen:
        maxlen = len(text)

for (text, number) in statistics:
    print(f"{text + ' ' * (maxlen+1-len(text))}:{number}")

