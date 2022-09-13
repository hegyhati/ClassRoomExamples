def v3():
    s = " a   abcd"
    l = s.split(' ')

    i=0
    while i < len(l):
        while l[i] == '' :
            l.pop(i)
        i+=1

    print( " ".join(l) )

def v4():
    s = " a   asjkfh sdfskjhskj  s    sdfkshdfk"
    l = s.split(' ')

    for i in range(len(l)-1,-1,-1):
        if l[i] == '' :
            l.pop(i)

    print( " ".join(l) )

def v5():
    s = " a   asjkfh sdfskjhskj  s    sdfkshdfk"
    l = s.split(' ')

    for i in range(len(l))[::-1]:
        if l[i] == '' :
            l.pop(i)

    print( " ".join(l) )

def v6():
    s = " a   asjkfh sdfskjhskj  s    sdfkshdfk"
    l = s.split(' ')

    while '' in l:
        l.remove('')
        
    print( " ".join(l) )

def v7():
    s = " a   asjkfh sdfskjhskj  s    sdfkshdfk"
    l = s.split(' ')

    try: 
        while True:
            l.remove('')
    except ValueError:
        pass
        
    print( " ".join(l) )

def v8():
    s = " a   asjkfh sdfskjhskj  s    sdfkshdfk"
    l = s.split(' ')

    l2 = [ w for w in l if w != '' ]
        
    print( " ".join(l2) )


print( " ".join([ w for w in input().split(' ') if w != '' ]) )