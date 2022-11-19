# BLAKE2 
from hashlib import blake2b
from hmac import compare_digest

KEY = b'testkey'
AUTH_SIZE = 16

def sign(cookie):
    return blake2b(cookie, key=KEY, digest_size=AUTH_SIZE).hexdigest().encode('utf-8')

def verify(cookie, sig):
    return compare_digest(sig, sign(cookie))

cookie = b'0xpacman'
sig = sign(cookie)

print("{0},{1}".format(cookie.decode('utf-8'), sig))

print(verify(b'1xpacman', sig))
# it will retrun False
print(verify(b'0xpacman', sig))
# returns True
