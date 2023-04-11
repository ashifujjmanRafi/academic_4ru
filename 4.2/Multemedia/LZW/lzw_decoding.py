f = open("lzw-compression.txt", "r")

arr_old = f.read().split(', ')
# print(arr_old)

arr = []
for i in range(len(arr_old)):
	arr.append(int(arr_old[i]))
	# print(arr_old[i])

dictionary = {}
for i in range(256):
	dictionary[i] = chr(i)

last = 256
result = ""

s = None

# print(dictionary[256])

for k in arr:
	try:
		entry = dictionary[k]
	except:
		entry = None
	finally: 
		if (entry == None):
			entry = s + s[0]
		
		result += entry

		if (s != None):
			dictionary[last] = s + entry[0]
			last += 1
		
		s = entry

# print(entry)

# result += entry

f = open("lzw-decompression.txt", "w")
f.write(result)
