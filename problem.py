age = int(input("enter your age "))
if( age in range(14)):
    print("you are a kid ")

elif  (age in range(13,20)):
    print("you are a teenager ")

elif (age in range(20,60)):
    print("you are an adult ")

elif (age>=60):
    print("you are senior ")

else:
    print("age is in valid ")
