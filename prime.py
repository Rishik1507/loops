n=int(input("Enter the number: "))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not a prime no.")
            break
    else:
        print("Prime No.")
else:
    print("The number is neither prime nor composite.")
