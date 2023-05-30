t = int(input())

for _ in range(t):
    n, cap = map(int, input().split())
    weights = list(map(int, input().split()))
    
    items = [(weights[i], i+1) for i in range(n)]
    items.sort()
    
    res = []
    cs = 0
    for item in items:
        cur = item[0]
        which = item[1]
        tst = cs + cur
        
        if 2 * tst < cap:
            cs += cur
            res.append(which)
        elif cap <= 2 * tst and tst <= cap:
            cs += cur
            res.append(which)
            break
        elif cur <= cap:
            cs = cur
            res = [which]
            break
        else:
            res = []
            break
    
    if cap <= 2 * cs and cs <= cap and res:
        print(len(res))
        print(*res)
    else:
        print("-1")
