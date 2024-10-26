#activity2: find the prime numbers
minimum=int(input("enter the mimimum value"))
maximum=int(input("enter your maximum value"))

for n in range(minimum,maximum+1):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            print(n)