n=input("Enter  no.")
a=0
for i in n:
    a+=int(i)**3

if a==int(n):
    print("Armstrong No.")
else:
    print("Npt an Armstrong No.")
