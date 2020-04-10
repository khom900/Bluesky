import random
def fx(op): # use Lambda
    if op=='+':
        return lambda a, b: a + b 
    else:
        return lambda a, b: a - b

def fx2(op):  # use inner function
    def add(a, b): return a + b
    def subtract(a, b):  # ขื้นหวัแถวไหม่
        return a - b
    if op == '+':
        return add
    else:
        return subtract
def fx3(op):   # ถ้าบ่มีโตนี้ เราต้องได้ขงน if เข้าไปๆลๆ
    d = {
        '+' : lambda a, b: a + b,
        '-' : lambda a, b: a - b,
        '*' : lambda a, b: a * b,
        '/' : lambda a, b: a / b,
        '^' : lambda a, b: a ** b # ขื้นกำลัง สอง
    }
    return d[op]
if __name__ == '__main__':
    # func=fx('+')
    # func=fx2('-')
    # print(func(5, 3))
    # func= fx3('*')
    # print(func(5, 3))
    for _ in range(6):
        op = random.choice(['+','-','*', '/', '^'])
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        func = fx3(op)
        print(f'{a:3} {op} {b:3} = {func(a, b):7}')


    
    