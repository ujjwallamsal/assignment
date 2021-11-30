#Program to Check if a Number is Positive, Negative or 0

# a = float(input("enter a number"))
# if a == 0 :
#     print("the number is zero")
# elif a<0:
#     print("the number is negative")
# else:
#     print("the number is positive")


# Program to Check if a Number is Odd or Even
# n = float(input("enter a number"))
# if (n%2) ==0:
#     print("it is even number")
# else:
#     print("it is odd number")


# Program to Find the Largest Among Three Numbers
# num1 = float(input("enter first number"))
# num2 = float(input("enter second number"))
# num3 = float(input("enter third number"))
# if (num1 >= num2) and (num1 >=num3):
#     print("num1 is the largest among three numbers")
# elif(num2 >= num1) and (num2 >= num3):
#     print("num2 is the largest among three numbers")
# else :
#     print("num3 is the largest among three numbers")

# 4. Program to Take in the Marks of 5 Subjects and Display the Grade

sub1 = float(input("enter the  marks in fist subject"))
sub2 = float(input("enter the  marks in second subject"))
sub3 = float(input("enter the  marks in third subject"))
sub4 = float(input("enter the  marks in fourth subject"))
sub5 = float(input("enter the  marks in fifth subject"))
avg = ((sub1 + sub2 + sub3 + sub4 + sub5)/5)
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: E")
