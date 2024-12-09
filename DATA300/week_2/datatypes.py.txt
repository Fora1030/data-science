#Key Python Variable Types
#Text Type:	str; you can use single quotes or double quotes
str1 = "Hello to you"
str2 = 'and Good morning'
#You can display variables with print()
print(str1, str2)
#and you can use type() to get the type of a variable
print('variable str1 var has type:', type(str1))
#Numeric Types:	int, float, complex
#int
num1 = 6
print('variable num1 has type:',type(num1))
#float
num2=1.3
print('variable num2 has type:',type(num2))
type(num2)
#Sequence Types:	list, tuple, range
#a list
list1 = ['hello','to','you']
print('variable list1 has type:',type(list1))
#lists support different types of elements
list2 = ['hello',1,'you',6.3,'yes',7,2.3]
#equivalent
list3 = list(('hello',1,'you',6.3,'yes',7,2.3))
#you can print elements of the string
#first element is list2[0] and last is list2[len(list2)-1]
#len() gives you the length---but since we start at 0, we have to subtract one
print(list2[0],list2[len(list2)-1])
print("list2:",list2[0], list2[1],list2[4:6])
print("list3",list3[0], list3[1],list3[4:6])
print('variable list2 has type:',type(list2))
#Now we modify the first element of list2
list2[0] = 'Yes indeed'
#and we see the list changed
print('list2=',list2)

#This example loops through all items of list3
#and if they are of type str, then it appends 'of course'
for i in range(len(list3)):
  if str(type(list3[i])) == "<class 'str'>":
    list3[i]=list3[i] + " of course"
print('list3=',list3)

#A tuple is similar to a list but the elements are immutable
tuple1 = ('hello',1,'you',6.3,'yes',7,2.3)
print(tuple1,type(tuple1))
#But if we try to change an element we get an error
#TypeError: 'tuple' object does not support item assignment
#Uncomment this next line to see the error:
#tuple1[0]='Yes indeed'
#Boolean Type:	bool
bool1 = True
bool2 = False
#we get false for this comparison
print("This should be false:", bool1 == bool2)
#and we get true for this one
print("This should be True:",bool2 == bool2)

#strings
#numbers

#NOTE: you will be graded on the following:
print("-"*100, "\n Graded activity:\n", "-"*100)

#Exercise on Python Data Types:
#1. Read, study and execute datatypes.py; you can copy the entire code from the file 
# or from the word document or parts of it into code blocks in a Jupyter workbook and execute it there.
# You can also copy the code into a Python IDE, like Spyder (from anaconda) \
# and execute it there.
#2. Modify the following code, such that if the elements are of type float,
#       then add 5 to the previous value:
#    This code loops through all items of list3
#    and if they are of type str, then it appends 'of course'
#    Notice that when we indent statements we should hit tab
#   Before you modify the code below try to guess what your output will be...
#Add at least two comments describing functioning of the code below

list3 = list(('hello',1,'you',6.3,'yes',7,2.3))

for i in range(len(list3)):
  # using the isinstance() function is pythonic and has better performance than using type()
  if isinstance(list3[i], float):
    # changes the previous value of the float by adding 5
    list3[i] =list3[i] + 5
  elif isinstance(list3[i], str):
    list3[i]=list3[i] + " of course"
print('list3=',list3)
# expected_output ['hello of course', 1, 'you of course', 11.3, 'yes of course', 7, 7.3]

#End of Exercise on Python Data Types
