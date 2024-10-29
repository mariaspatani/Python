number=int(input("enter a number"))
isPrime= True
for i in range (2,(number//2)+1):
    if number%i==0:
        isPrime= False
        break
if isPrime:
        print("prime")
else:
    print("not prime")