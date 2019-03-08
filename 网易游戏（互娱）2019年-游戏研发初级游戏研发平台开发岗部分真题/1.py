n = int(input())

for _ in range(n):
    d = input().strip()
    hh, mm, ss = map(int, list(d.split(':')))
    if hh>23:
        hh = hh % 10
    if mm > 59:
        mm = mm % 10
    
    if ss>59:
        ss = ss % 10
    
    print('{:0>2d}:{:0>2d}:{:0>2d}'.format(hh, mm, ss))
