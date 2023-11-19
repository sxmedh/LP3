def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    first=0
    second=1

    while n-2>=0:
        third = first + second
        first=second
        second=third
        n-=1

    return third

if __name__=="__main__":
    n=10
    print(recursive_fibonacci(n))
    print(non_recursive_fibonacci(n))