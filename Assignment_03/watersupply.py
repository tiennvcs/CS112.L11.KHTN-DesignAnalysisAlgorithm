import sys
sys.setrecursionlimit(10**6)
modulo = 10**9 + 7
(n , m) = map(int,(input().split()))
graph = {}
##for i in range(m):
##    (u ,v ) = map(int, (input().split()))
##    graph[u].append(v)
##    graph[v].append(u)
for _ in range(m):
    u, v = map(int, input().split())
    try:
        graph[u].append(v)
    except:
        graph[u] = [v]
    try:
        graph[v].append(u)
    except:
        graph[v] = [u]
mark = [True] * (n+10)
number = []
def dfs(u):
    mark[u] = False
    number[len(number)-1] += 1
    if u not in graph:
        return
    for v in graph[u]:
        if (mark[v] == True):
            dfs(v)

for i in range(1, n+1):
    if (mark[i] == True):
        number.append(0)
        dfs(i)
#print(number)
idx = len(number)
print(idx - 1)
if idx > 1:
    ans = 1
    for num in number:
        ans = ((ans % modulo) * (num % modulo)) % modulo
    for i in range(idx-2):
        ans = ((ans % modulo) * (n % modulo)) % modulo
    print(ans % modulo)
else:
    print(0)
