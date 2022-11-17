data = dict()
arr = []
for num in [4, 3, 2, 7, 8, 2, 3, 1]:
    if data.get(num) is None:
        data[num] = 1
        continue
    arr.append(num)
print(arr)
