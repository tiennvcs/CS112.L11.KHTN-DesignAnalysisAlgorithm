s1 = input()
s2 = input()
B_pairs = set()
result = 0
for i in range(len(s2) - 1):
  item = s2[i:i+2]
  B_pairs.add(item)

for i in range(len(s1) - 1):
  item = s1[i:i+2]
  if item in B_pairs:
    result += 1
print(result)
