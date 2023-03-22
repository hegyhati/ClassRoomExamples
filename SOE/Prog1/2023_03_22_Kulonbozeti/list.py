data = [1,2,3,4,1,2,3,"NA",4,5,"NA",12,43,"NA",45]

while "NA" in data:
    data.remove("NA")

sum_of_data = 0
for item in data:
    sum_of_data += item

print(f"average: {sum_of_data/len(data):.6}")
print(f"average: {sum(data)/len(data):.6}")
print(f"max: {max(data)}")
print(f"min: {min(data)}")


scaled_data = data[:]

for idx,value in enumerate(scaled_data):
    scaled_data[idx] = 100 * (value - min(data)) / (max(data) - min(data))

print(scaled_data)




