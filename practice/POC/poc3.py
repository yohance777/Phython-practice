num = (input("Enter a password: "))
length = len(num)
has_digit = False
has_special = False
if length < 8:
    print("password shold contain 8 char")
else:
        for char in num:
             if char.isdigit():
                 has_digit = True           
                 
            
                    
                    
if has_digit:
    print("valid")
else:
    print("sorry,retry")
                
        



    
