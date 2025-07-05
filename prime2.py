#check if a given number is prime or not
n = int(input("enter number"))
if n <= 1:
    print(n," is not a prime number")
else:
    i = 2
    while i <= n // 2:
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")