x1 = int(input("Enter x coordinate of pt. A.\n"))
y1 = int(input("Enter y coordinate of pt. A.\n"))
x2 = int(input("Enter x coordinate of pt. B.\n"))
y2 = int(input("Enter y coordinate of pt. B.\n"))
x3 = int(input("Enter x coordinate of pt. C.\n"))
y3 = int(input("Enter y coordinate of pt. C.\n"))
x = int(input("Enter x coordinate of pt. P.\n"))
y = int(input("Enter y coordinate of pt. P.\n"))
a = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
a1=(x1*(y2-y)+x2*(y-y1)+x*(y1-y2))/2 #area of PAB
a2=(x*(y2-y3)+x2*(y3-y)+x3*(y-y2))/2 #area of PBC
a3=(x1*(y-y3)+x*(y3-y1)+x3*(y1-y))/2 #area of PAC
if a==a1+a2+a3:
    print("P lies inside triangle ABC.")
else:
    print("P does not lie inside triangle ABC.")


