a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))
d = float(input("Enter number d: "))
list = [a,b,c,d]
sum = 0
multiple = 1
for i in list:
    sum += i
    multiple *= i
d = a - b - c - d
if sum % 1 == 0:
    sum = int(sum)
if multiple % 1 == 0:
    multiple = int(multiple)
if d % 1 == 0:
    d = int(d)
print("Sum equal to " + str(sum))
print("Multiple equal to " + str(multiple))
print("Difference equal to " + str(d))
