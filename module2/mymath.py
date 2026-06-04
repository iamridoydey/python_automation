def sum(a, b) -> int:
    return a + b

def division(a, b) -> float:
    if a == 0 or b == 0:
        return 0

    return a / b

def sub(a, b) -> int:
    return a - b

def multi(a, b) -> int:
    return a * b

def pow(a, b) -> int:
    return a << (b - 1)