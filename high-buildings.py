# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73
for i in range(int(input())):
    n,andre,sule,both = map(int, input().split())
    
    a = [1]*n
    #if andre == sule and andre != both:
    #    print('IMPOSSIBLE')
    #    continue
    if andre == n:
        if andre == sule and andre == both:
            a = [n] * n
        else:
            print("Case #{}: IMPOSSIBLE".format(i + 1))
            continue
    
    #if andre == sule:
    for j in range(both):
        if andre <= sule:
            a[andre - (j + 1)] = n
            #print("{}:{}".format(andre - (j + 1),n))
        else:
            a[andre + j] = n
            #print("{}:{}".format(andre+j,n))
    
    for j in range(andre - both):
        a[(andre - both) - (j + 1)] = n - (j + 1)
        #print("{}: {}".format((andre - both) - (j + 1),n-(j + 1)))
    
    for j in range(sule - both):
        a[-(sule - both) + j] = n - (j+1)
        #print("{}: {}".format(-(sule - both) + j,n-(j + 1)))
        #print(-(sule - both) + (j - 1))
    print("Case #{}: ".format(i+1),end='')
    print(*a)
