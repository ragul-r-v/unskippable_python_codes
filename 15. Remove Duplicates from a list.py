numbers = [1, 2, 2, 3, 1, 4, 3]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)