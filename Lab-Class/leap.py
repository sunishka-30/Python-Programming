y=int(input("Enter the year.\n"))
if y%400==0:
    print("Leap year.")
elif y%100!=0 and y%4==0:
    print("Leap year.")
else:
    print("Not a leap year.")