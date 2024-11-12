#program to check if the string is the same as the input string

def check_string(input_string):
    
    user_input= input("Enter a string:")
    
    if input_string == user_input:
        return True
    else:
        return False
    
    result = check_string("hello")
    print(result)
    
    input_string()