p = float(input("Enter principal ammount: "))
t = float(input("Enter time duration in years: "))
r = float(input("Enter the annual interest rate: "))

ammount = p*((1+r)/100)**t

ci = ammount - p

print("Compound interest is = ",ci)