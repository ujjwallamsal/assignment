# program to print average of numbers

a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
d = int(input("Enter number"))
sum = a + b + c + d
average = sum / 4
print("the average of numbers is : ", average)

# Program to Exchange the Values of Two Numbers With Using a Temporary Variable

x = 5
y = 10
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a = 11
b = 7
a, b = b, a
print(a) 
print(b) 

# Program to Read a Number n and Compute n+nn+nnn
n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

# Program to Read Two Numbers and Print Their Quotient and Remainder
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
quotient=a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)

print(remainder)