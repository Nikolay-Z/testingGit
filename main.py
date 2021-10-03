"""Generate and print random password of given length"""

import random

passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890"
p =  "".join(random.sample(s, passlen))
print(p)
