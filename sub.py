a,b,c = 4,3,4

input = [a,b,c]

sorted_intput = sorted(input,reverse=True)

def isvalid(input):
    if input[0]-1 >= 0 and input[1]-1 >= 0:
        return True
    else:
        return False

def getsub(input):
    output = [input[0] -1 ,input[1] -1 , input[2]]
    return sorted(output,reverse=True)

final=[]

while isvalid(sorted_intput):
    tmp=getsub(sorted_intput)
    final.append(tmp)
    sorted_intput=tmp

print(final)