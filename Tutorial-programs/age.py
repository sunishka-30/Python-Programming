print("What is your age?")
age = int(input())
if age>=7 and age<=100:
   if age<18:
       print("You cannot drive")

   elif age==18:
       print("We will think about you")

   else:
       print("You can drive")
else:
    print("Invalid age")