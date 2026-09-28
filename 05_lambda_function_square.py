def arg(x):
    return x * x

n = int(input("Enter a number: "))

print("Square using normal function:", arg(n))

# Lambda function

print("Square using lambda:", (lambda x: x * x)(n))