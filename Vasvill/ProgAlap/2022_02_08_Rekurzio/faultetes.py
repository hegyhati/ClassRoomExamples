def faultetes_1(n):
    makk = 1
    kisfa = 0
    nagyfa = 0

    for nap in range(2, n+1):
        nagyfa = kisfa + nagyfa
        kisfa = makk
        makk = nagyfa
        print(nap, ". ev:", "makk:", makk, "kisfa:", kisfa, "nagyfafa:", nagyfa)


def faultetes_2(n):
    kisfa = 1
    nagyfa = 0
    for nap in range(3, n+1):
        tmp = nagyfa
        nagyfa = nagyfa+kisfa
        kisfa = tmp
        print(nap, ". ev:", "makk:", nagyfa,
              "kisfa:", kisfa, "nagyfafa:", nagyfa)


def faultetes_3(n):
    elozonagyfa = 0
    mostaninagyfa = 1
    for nap in range(4, n+1):
        tmp = elozonagyfa
        elozonagyfa = mostaninagyfa
        mostaninagyfa = tmp + mostaninagyfa

        print(nap, ". ev:", "makk:", mostaninagyfa, "kisfa:",
              elozonagyfa, "nagyfafa:", mostaninagyfa)


def nagy_fa_szam(n):
    if n == 3:
        return 1
    elif n == 2:
        return 0
    else:
        return nagy_fa_szam(n-1)+nagy_fa_szam(n-2)

def faultetes_4(n):
    makk = [0]*(n+1)
    kisfa = [0]*(n+1)
    nagyfa = [0]*(n+1)

    makk[0]=1

    for ev in range(1,n):
        nagyfa[ev+1] = kisfa[ev] + nagyfa[ev]
        kisfa[ev+1] = makk[ev]
        makk[ev+1] = nagyfa[ev+1] 

    print(makk, kisfa, nagyfa)

def faultetes_6(n):
    nagyfa = [0]*n
    nagyfa[1]=1
    for ev in range(2,n):
        nagyfa[ev]=nagyfa[ev-1]+nagyfa[ev-2]
    print(nagyfa)

faultetes_6(10)
print(nagy_fa_szam(20))
