#inbuilt
int(),float(), bool()
#inbuilt 2
from math import *
print(sqrt(160))

# user defined
def p_sum(first, second):
    return first+second
print(p_sum(1,2))

def p_sum(first, second=2):
    return first+second
print(p_sum(1))