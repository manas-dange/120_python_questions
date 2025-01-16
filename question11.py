#11
p = int(input("Enter principal amount"))
r = int(input("Enter rate of interest"))
t = int(input("Enter years"))
ci = p*((1+(r/100))**t)-p
print(ci)