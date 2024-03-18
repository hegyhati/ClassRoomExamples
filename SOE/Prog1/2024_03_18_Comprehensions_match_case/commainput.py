# input: marko ATTILA, SZEKERES aDaM, kAtOnA Krisztian
# output:
# Bejott: Marko Attila
# Bejott: Szekeres Adam
# Bejott: Katona Krisztian

names = input("Kik jottek be? (vesszovel elvalasztva:)")
names = [ name.strip() for name in names.split(",") ]
    
for name in names:
    print(f"Bejott: {name}")
    