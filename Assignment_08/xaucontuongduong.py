import sys
s=[0]+list(sys.stdin.readline().strip())
queries=int(sys.stdin.readline())
h={}
for i in range(97,123):
    h[chr(i)]=1<<(i-97)
for i in range(1,len(s)):
    s[i]=s[i-1]+h[s[i]]
for query in range(queries):
    a,b,c,d=map(int,sys.stdin.readline().split())
    if (s[b]-s[a-1]==s[d]-s[c-1]):
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
