#2
def countdown (n):
    for i in range(n,0,-1):
        yield i
print(list(countdown(5)))        

double = (i**2 for i in range(1,10+1))
print(list(double))
print("-"*20)
def dob(n):
    for i in range(1,n+1):
        yield i ** 2
print(list(dob(10)))        