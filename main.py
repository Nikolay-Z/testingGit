"""Generate random password of given length"""

def random_password(length):
    import random
    
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s, length))
    print(p)