t = int(input())

for _ in range(t):
    _ = input()
    
    data = (input().strip().split(' '))
    table = dict()
    ans = []
    for k in data[::-1]:
        if k not in table:
            table[k] = 1
            ans.append(k)
    print(' '.join(ans))
