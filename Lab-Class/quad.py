import math
a=int(input("Enter root.\n"))
b=int(input("Enter root.\n"))
c=int(input("Enter root.\n"))
dis = b * b - 4 * a * c
print("Discriminant = ",dis)
sqrt_val = math.sqrt(abs(dis))
if dis > 0:
    print("Real and Different Roots ")
    print((-b + sqrt_val) / (2 * a))
    print((-b - sqrt_val) / (2 * a))

elif dis == 0:
    print("Real and Same Roots")
    print(-b / (2 * a))
else:
    print("Complex Roots")
    print(- b / (2 * a), " + i", sqrt_val)
    print(- b / (2 * a), " - i", sqrt_val)
