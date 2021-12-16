Program to Check if a Number is Positive, Negative or 0 using function
def num():
    num = int(input("enter a number"))
    if num > 0:
        print("It is positive number")
    elif num == 0:
        print("It is Zero")
    else:
        print("It is a negative number")
num()
   


Program to Check if a Number is Odd or Even using function

def evenodd():
    a = int(input("enter a number"))
    if (a % 2 == 0):
        print("it is even number")
    else:
        print("it is odd number")
evenodd()


Program to Find the Largest Among Three Numbers using function
def largest():
    a = int(input("enter a first number"))
    b = int(input("enter a second number"))
    c = int(input("enter a third number"))
    if a>b>c:
        print(" a is greater among three number")
    elif b>c>a:
        print("b is greater among three number")
    else:
        print("c is greater among three numbers")
largest()

Program to Take in the Marks of 5 Subjects and Display the Grade using function

def grade():
    sub = int(input("Enter marks of the first subject: "))
    sub1 = int(input("Enter marks of the second subject: ")) 
    sub2 = int(input("Enter marks of the third subject: "))
    sub3 = int(input("Enter marks of the fourth subject: "))
    sub4 = int(input("Enter marks of the fifth subject: "))
    avg=(sub+sub2+sub3+sub4+sub1)/5
    if(avg>=90):
        print("Grade: A")
    elif(avg>=80 and avg<90):
        print("Grade: B")
    elif(avg>=70 and avg<80):
        print("Grade: C")
    elif(avg>=60 and avg<70):
        print("Grade: D")
    else:
        print("Grade: E")
grade()


Program to Find the Sum of Natural Numbers using function

def num():
    num = int(input("enter a number"))
    if num < 0:
        print("enter a positive number")
    else:
        sum = 0
        while(num>0):
            sum+= num
            num-=1
        print("the sum of natural number is: " , sum)
num()


Program to make a simple calculator using functions

def add(P, Q):      
   return P + Q   
def subtract(P, Q):    
   return P - Q   
def multiply(P, Q):   
   return P * Q   
def divide(P, Q):      
   return P / Q     
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
choice = input("Please enter choice (a/ b/ c/ d): ")    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
elif choice == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")    


Program to display calendar using calendar module

import calendar
yy = 2020
mm = 11
print(calendar.month(yy, mm))