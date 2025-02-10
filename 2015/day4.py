import hashlib

input = 'yzbqklnj'

i = 1
hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
while True:
    if hash.startswith('00000'):
        break
    i += 1
    hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
print(i)
print(hash)
