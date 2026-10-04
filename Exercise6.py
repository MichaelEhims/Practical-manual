#Exercise 1
n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        
#Exercise 2
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end ="\t")
    print()