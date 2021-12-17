# Program to interchange first and last elements in a list
def swapList(List):
	List[0], List[-1] = List[-1], List[0]
	return List
List = [12, 35, 9, 56, 24]
print(swapList(List))

# Program to swap two elements in a list
list = [1 , 3 ,7 ,9]
list[0],list[2] = list[2] , list[0]
print(list)
# Program to Reverse a List
l = [1 , 5 , 3, 5, 7]
a = l[::-1]
print(a)

# Program to find sum of elements in list
total = 0
list1 = [11, 5, 7, 1, 3]
for ele in range(0, len(list1)):
	total = total + list1[ele]
print("Sum of all elements in given list: ", total)

# Program to find greatest number in a list
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

# Program to Count occurrences of an element in a list

def countX(lst, x):
    result = lst.count(x)
    return result
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
result = countX(lst, x)
print(result)