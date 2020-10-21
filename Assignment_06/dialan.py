def checkBit(bit):
    for i in range(12):
        if bit[i]==1:
            return 0
    return 1
import sys
n,k=map(int,input().split())
arr=list(map(int,input().split()))
bit=[0]*n
for i in range(n):
    bit[i]=list(map(int,bin(arr[i])[2:].zfill(12)))
res=[1]*12
def findTheBest(res):
    idx=0
    maxnum=0
    for i in range(n):
        num=0
        for j in range(12):
            num+=res[j]*(res[j]^bit[i][j])
        if maxnum<num:
            maxnum=num
            idx=i
    return idx,maxnum
idx,num=findTheBest(res)
res=bit[idx][:]
check=checkBit(res)
if check==1:
    print('YES')
    sys.exit()
k-=1
while k>0:
    #Find index
    idx,num=findTheBest(res)
    if num==0:
        break
    #Merge the best with res
    for j in range(12):
        res[j]=res[j]&bit[idx][j]
    check=checkBit(res)
    if check==1:
        print('YES')
        sys.exit()
    k-=1
print('NO')
