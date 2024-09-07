def simplest(limit):
    for number in range(1,limit+1):
        n = number
        while n != 1:
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        if number % 1000 == 0:
            print(number)

def cache_list(limit):
    known = []
    for number in range(1,limit+1):
        new = []
        n = number
        while n != 1:
            if n in known: break
            new.append(n)
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        known.extend(new)
        if number % 1000 == 0:
            print(number)

def cache_sorted_list(limit):
    known = []
    for number in range(1,limit+1):
        new = []
        n = number
        while n != 1:
            if n in known: break
            new.append(n)
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        known.extend(new)
        known.sort(reverse=True)
        if number % 1000 == 0:
            print(number)

def cache_semi_sorted_list(limit):
    known = []
    for number in range(1,limit+1):
        new = []
        n = number
        while n != 1:
            if n in known: break
            new.append(n)
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        for item in new:
            known.insert(0,item)
        if number % 1000 == 0:
            print(number)

def cache_set(limit):
    known = set()
    for number in range(1,limit+1):
        new = []
        n = number
        while n != 1:
            if n in known: break
            new.append(n)
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        known.update(new)
        if number % 1000 == 0:
            print(number)

def clever_cache_set(limit):
    known = set()
    for number in range(1,limit+1):
        new = []
        n = number
        while n != 1:
            if n < number: break
            if n in known: break
            new.append(n)
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        known.update(new)
        if number % 1000 == 0:
            print(number)

def clever(limit):
    for number in range(2,limit+1):
        n = number
        while n >= number:
            if n % 2 == 0: n//=2
            else: n = 3 * n + 1
        #if number % 1000 == 0:
        #    print(number)

def very_clever(limit):
    for number in range(2,limit+1):
        n = number
        while n >= number:
            if n % 2 == 0: n//=2
            else: n = (3 * n + 1)//2
        #if number % 1000 == 0:
        #    print(number)

#simplest(10_000_000) # 1:02
#cache_list(10_000_000) # way tooo slow
#cache_sorted_list(10_000_000) # even slower
#cache_semi_sorted_list(10_000_000) # bit faster... maybe
#cache_set(10_000_000) # Woah 0:06
#clever_cache_set(10_000_000) # Bit slower
#clever(10_000_000) # 0:02
very_clever(10_000_000) # 0:01.6