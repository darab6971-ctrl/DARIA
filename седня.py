t=input(" ")
result={}
for key in t:
    if key in result:
        result[key]+=1
    else:
        result[key]=1
print(result)

a=[{'ww': 67, 'x': '', 'z': []}]
result=[]
for i in a:
    if isinstance(i, dict):
        ndict={}
        for key, value in i.items():
            if value or value==0:
                ndict[key]=value
        if ndict:
            result.append(ndict)
a=result
print(a)
