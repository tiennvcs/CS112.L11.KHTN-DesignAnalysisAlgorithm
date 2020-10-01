from bisect import bisect_left as lower_bound

n = int(input())
a, b, c, d = map(int,input().replace('/',' ').split())

points = [map(int,input().split()) for _ in range(n)]
rpoints = [(-a*x+b*y,-(-c*x+d*y)) for x,y in points]
spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))

F = []
for x,y in spoints:
    i = lower_bound(F,y)
    if i == len(F):
        F.append(y)
    else:
        F[i] = y

print(len(F))