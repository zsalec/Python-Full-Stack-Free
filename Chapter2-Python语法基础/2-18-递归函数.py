# recursion 递归

def funca():
    print('function a')
    return None


def funcb():
    funca()
    print('function b')
    return None


funcb()


# - factorial
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('5! =', factorial(5))  # 5! = 120
print('10! =', factorial(10))  # 10! = 3628800


# - 递归必须要有结束条件

# - Fibonacci 斐波那契数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return n + fibonacci(n - 1)


print('fibonacci(10) = {}'.format(fibonacci(10)))  # fibonacci(10) = 53
print('fibonacci(100) = {}'.format(fibonacci(100)))  # fibonacci(100) = 5048


# - Tower of Hanoi 汉诺塔
def hanoi(a, b, c, n):
    if n == 1:
        print('{} --> {}'.format(a, c))
    else:
        hanoi(a, c, b, n - 1)
        print('{} --> {}'.format(a, c))
        hanoi(b, a, c, n - 1)
    return None


def testHanoi(a, b, c, n):
    print('Hanoi (level {})'.format(n))
    hanoi(a, b, c, n)
    return None


a = 'A'
b = 'B'
c = 'C'
testHanoi(a, b, c, 1)
'''
Hanoi (level 1)
A --> C
'''
testHanoi(a, b, c, 2)
'''
Hanoi (level 2)
A --> B
A --> C
B --> C
'''
testHanoi(a, b, c, 3)
'''
Hanoi (level 3)
A --> C
A --> B
C --> B
A --> C
B --> A
B --> C
A --> C
'''
