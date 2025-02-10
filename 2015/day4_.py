import hashlib

input = 'yzbqklnj'

i = 1
hash = hashlib.md5((input + str(i)).encode('utf-8'))
while not hash.hexdigest().startswith('000000'):
    i += 1
    hash = hashlib.md5((input + str(i)).encode('utf-8'))

print(i)
print(hash.hexdigest())
