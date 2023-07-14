
f = open("compressed.txt","r")
arr_old = f.read().split(", ")
arr = [int(x) for x in arr_old]

dic = {}
for i in range(256):
    dic[i]=chr(i)
last = 256
result = ""
s = None
for k in arr:
    try:
        entry = dic[k]
    except:
        entry = None
    finally:
        if(entry== None):
            entry = s+s[0]
        result += entry
        if(s!=None):
            dic[last]=s+entry[0]
            last+=1
        s=entry
f = open("decompressed.txt","w")
f.write(result)
        


        
