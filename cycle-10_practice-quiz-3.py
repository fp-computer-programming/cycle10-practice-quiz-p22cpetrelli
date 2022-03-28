#author CJP 01/27/2022
def fibonacci(num):
    x = 2 
    ans = [0,1]

    while x < num:
            ans.append(ans[-2] + ans[-1]) 
            x += 1

    return ans

print(fibonacci(5) == [0,1,1,2,3])
print(fibonacci(10) == [0,1,1,2,3,5,8,13,21,34])