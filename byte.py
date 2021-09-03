#byte literals
b=b'abc'
b1=b"abc"
b2=b"""abc"""
b3=b'''abc'''
b4=b'xyz'
b5=b'\yz'
s='abc'
print('b:','b','type:',type(b))
print('b1:','b','type:',type(b1))
print('b2:','b','type:',type(b2))
print('b3:','b','type:',type(b3))
print('b4:','b','type:',type(b4))
print('b5:','b','type:',type(b5))
print('s:','s','type:',type(s))
print('b[0]:',b[0])
print('b4[0]:',b4[0])
print('b5[0]:',b5[0])
print('s[0]:',s[0])
print(bytes(10))
print(bytes(10))
print(bytes(range(20)))
print(bytes(range(256)))
#for i in bytes(range(256)):
    #print(chr(i))
print(ord('!'))
#1
b=b'python programming'
for i in b:
    print(i,hex(i),bin(i))
#Binary literals:
b='abc'
b1=b"abc"
b2=b"""abc"""
b3=b'''abc'''
b4=b'xyz'
b5=b'\yz'
ba=bytearray(b)
ba1=bytearray(b1)
ba=bytearray(b2)
ba=bytearray(b3)
ba=bytearray(b4)
ba=bytearray(b5)
print('ba:',ba,'type:',type(ba))
print('ba1:',ba,'type:',type(ba1))
print('ba2:',ba,'type:',type(ba2))
print('ba3:',ba,'type:',type(ba3))
print('ba4:',ba,'type:',type(ba4))
print('ba5:',ba,'type:',type(ba5))
print('s:','s','type:',type(s))
print('ba[0]:',ba[0])
print('ba4[0]:',ba4[0])
print('ba5[1]:',ba5[1])
print('s[0]:',s[0])
print(bytearray(10))
print(bytearray(range(20)))
print(bytearray(range(256))
#3
b=b'python programming'
ba=bytearray(b)
ba[0]=ord('p')
for i in ba:
    print(i,hex(i))
print(ba)
