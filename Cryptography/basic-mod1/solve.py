import string
c = string.ascii_uppercase
c += "0123456789_"

arr = {128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140}
res = ""
for i in arr:
    res += c[i%37]

print('picoCTF{' + res +'}')


