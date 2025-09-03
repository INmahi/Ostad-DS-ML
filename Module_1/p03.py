#PROBLEM 3: Write a program using a for loop that calculates the sum of even numbers between 1 and 100.
sum = 0
for i in range(101):
    if i%2==0:
        sum += i
    else:
        continue

print(sum)