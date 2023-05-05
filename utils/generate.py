import random

def generate_code(n=8):
    num='123456789'
    code = ''.join(random.choice(num) for x in range(n))
    return code 

# print(generate_code())