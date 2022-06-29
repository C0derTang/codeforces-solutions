import io,os, sys, collections

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

#input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    if len(set(a)) == 1 and a[0] == 0:
        sys.stdout.write("0\n")
        continue
    
    a = collections.deque(a)

    while a and a[-1] == 0:
        a.pop()
    while a and a[0] == 0:
        a.popleft()

    if 0 in a:
        sys.stdout.write("2\n")
    else:
        sys.stdout.write("1\n")