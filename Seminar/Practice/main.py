MODULO = 1000000007
#Perform multipled matrix
def multiple(a, b):
    c = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MODULO
    return c

def divide(n):
    #Return the F[1] with n = 1
    if (n == 1):
        return [[0,1], [1,1]]
    #Calculate subproblem is half of n
    mul = divide(n//2)
    #Merge the subproblem, calculate two matrix by multiplying
    result = multiple(mul,mul)
    #If n is odd, multiple the F[1] with result
    if (n % 2 == 1):
        result = multiple(result, [[0,1],[1,1]])
    return result

#Input number of tests
Test = int(input())
#Input test case
for _ in range(Test):
    n = int(input())
    if (n == 0):
        print(0)
        continue
    #Perform divide and conquer with n number inputed
    result = divide(n)
    #Print the result with F[n] in matrix
    print(result[1][0])
