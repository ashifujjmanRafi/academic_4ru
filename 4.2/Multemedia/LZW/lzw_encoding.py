# f = open("input.txt","r")
# string = f.read()
# dic = {}
# for i in range(256):
#     dic[chr(i)] = i
# last = 256
# result = []

# s = string[0]
# string = string[1:]

# for c in string:
#     temp = s+c
#     if temp in dic :
#         s = temp
#     else:
#         result.append(dic[s])
#         dic[temp] = last
#         last += 1
#         s = c
        
# result.append(dic[c])

# result = str(result)
# result = result[1:-1]
# f = open("compressed.txt","w")
# f.write(result)

f = open("input.txt","r")
string = f.read()

dic = {}
for i in range(256):
    dic[chr(i)]=i
last = 256
result = []
s = string[0]
string = string[1:]

for c in string:
    temp = s+c
    if temp in dic:
        s = temp
    else:
        result.append(dic[s])
        dic[temp]=last
        last += 1
        s = c
result.append(dic[c])
result = str(result)
result = result[1:-1]
f = open("compressed.txt","w")
f.write(result)
        
    