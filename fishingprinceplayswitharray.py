"""
     ___
 _ /    _\_
/ |    |___|
| |       |
\_|   __  |
   \_/  \_/
  uwu amogus
"""

import io,os, sys, collections

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    k = int(input())
    b = [int(i) for i in input().split()]

    ap, bp = [], []

    for i in a:
        tmp = i
        while tmp % m == 0:
            tmp //= m
        if ap and ap[-1][0] == tmp:
            ap [-1][1] += i // tmp
        else:
            ap.append([tmp, i//tmp])
    
    for i in b:
        tmp = i
        while tmp % m == 0:
            tmp //= m
        if bp and bp[-1][0] == tmp:
            bp [-1][1] += i // tmp
        else:
            bp.append([tmp, i//tmp])
    
    if ap == bp:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
