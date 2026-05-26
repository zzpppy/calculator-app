def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b
def power(a, b):
    """计算 a 的 b 次方"""
    return a ** b

def mod(a, b):
    """计算 a mod b"""
    if b == 0:
        return "Error: modulus by zero"
    return a % b
if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))
    print(divide(1023231231,232))