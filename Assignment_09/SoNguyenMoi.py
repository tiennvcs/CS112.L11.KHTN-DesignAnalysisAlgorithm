# Cho so nguyen duong n khong qua 100 chu so
# Xac dinh so nguyen lon nhat m chia het cho 3 va khac n o dung mot chu so

# Xet moi hang don vi, tim ra cac so chia het cho 3
# Ket qua la so lon nhat duoc tim thay

num = input()
tong = 0
for i in num:
    tong += int(i)
ans = []
for i in range(len(num)):
    tong -= int(num[i])
    need = (3 - (tong % 3)) % 3
    for j in range(need,10,3):
        if (j != int(num[i])):
            ans.append(num[0:i] + str(j) + num[i+1:])
    tong += int(num[i])
ans.sort()
print(ans[len(ans)-1])
