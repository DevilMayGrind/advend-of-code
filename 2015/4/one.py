import hashlib

input = 'yzbqklnj'

i = 1
md5_hash = hashlib.md5((input + '1').encode('utf-8'))
while not md5_hash.hexdigest().startswith('00000'):
    i += 1
    md5_hash.update((input + str(i)).encode('utf-8'))
print(i)
print(md5_hash.hexdigest())
