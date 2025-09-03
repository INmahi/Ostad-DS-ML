numbers = [1, 5, 6, 5, 1, 2, 3]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)


print("Duplicate elements:", duplicates)
