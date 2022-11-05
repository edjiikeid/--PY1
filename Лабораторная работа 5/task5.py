import random
import time
import string


def get_random_password(x=8) -> str:
    str_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    str_ = random.sample(str_, x)
    return str_


s = ['1', 'r', 'A', ]
t = time.time()
k = 0
while get_random_password(3) != s:
    k += 1

print(k)
print(time.time() - t)
print(get_random_password())
