a = int(input("Enter number a "))
b = int(input("Enter number b "))
c = int(input("Enter number c "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Sorted values by increasing", a, b, c)