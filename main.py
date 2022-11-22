n = int(input())
a =[int(x) for x in input().split()]
b =[int(x) for x in input().split()]
a_min = min(a)
count = 0
i = 0
while i < n:
    if a[i] > a_min:
        a[i] = a[i] - b[i]

        count = count+1
    if a[i] == a_min:
        i=i+1
        continue
    if a[i] < b[i]:
        count = -1
        break
    if a[i] < a_min:
        a_min = a[i]
        i = 0
        continue
        i = i+1
print(count) 