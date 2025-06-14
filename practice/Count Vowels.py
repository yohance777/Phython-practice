import re

num1 = (input("enter the string"))
num2 = r"a" 
x = re.findall(num2, num1)
a = len(x)
print(a)

