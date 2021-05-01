out = {}

data = open('nginx.log').read()
data = data.splitlines()

for i in data:
    ip = i.split()[0]
    if ip not in out.keys():
        out[ip] = 1
    else:
        out[ip] +=1

print(out)
#print(out)
sorted_out = sorted(out.items(),reverse=True,key=lambda x: x[1])
for i in sorted_out:
    print('{} ==> {}'.format(i[0],i[1]))