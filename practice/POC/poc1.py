string = input("Enter the string: ")
length = len(string)
i = length - 1
reversed_string = ""

while i >= 0:
    reversed_string += string[i]
    i -= 1

print("Reversed string:", reversed_string)