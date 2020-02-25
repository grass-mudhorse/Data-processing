import random
import string
import re

def exo(n,s):
    random.seed(s)
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(n))
    return password

exo(10,30)

ph_num1 = '(01) 12 05 25, (04) 25 23 11, (08) 03 49 98'


rule = re.compile(r'[@](.*)')

ph_num1.split()
