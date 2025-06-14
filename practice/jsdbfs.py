num1 = input("Enter the number or word to check whether it's a palindrome: ")
length = len(num1)
print("Length:", length)

# Check if the input is a palindrome
i = 0
is_palindrome = True

while i < length // 2:
    if num1[i] != num1[length - i - 1]:
        is_palindrome = False
        break
    i += 1

if is_palindrome:
    print(f"'{num1}' is a palindrome.")
else:
    print(f"'{num1}' is not a palindrome.")