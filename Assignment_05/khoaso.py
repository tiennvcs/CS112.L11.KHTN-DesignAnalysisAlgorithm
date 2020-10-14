n = input()
digit=[0]*100
for i in range(len(n)):
    digit[ord(n[i])-48]+=1
tong=sum([(i*digit[i]) for i in range(10)])
if tong%3!=0:
    start=tong%3
    if tong%3 == 1:
        end=3
        step=1
    else:
        if tong%3==2:
            end=0
            step=-1
    for modnum in range(start,end,step):
        if tong%3==0:
            break
        so=modnum
        while so<10:
            while digit[so]>0 and tong%3!=0:
                digit[so]-=1
                tong-=so
            if tong%3==0:
                break
            so+=3
##Output
kq=''
for i in range(9,-1,-1):
    for j in range(digit[i]):
        kq+=chr(i+48)
print(kq)
