#author CJP 01/27/2022

def factorial(value):
    result = 1 
#counter
    x = 1 
    if value == 0:
        result = 0 
    else:
    #cant be greater than inself
        while x <= value: 
            result = x * result 
    #counter
            x += 1 
    return result

# test case
print(factorial(3))