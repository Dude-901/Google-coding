# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    temp = a[1] - a[0]
    diff = 0
    cnt = 1
    flag = 0
    for j in range(len(a)-1):
        diff = a[j+1] - a[j]
        if diff == temp:
            cnt += 1
        else:
            temp = diff
            if cnt > flag:
                flag = cnt
            cnt = 2
    print("Case #{}: {}".format(i+1,max(cnt,flag)))
