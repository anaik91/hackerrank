x ,y , z = 1,1,2
number = 3
combinatinos = []

i = [0,1]
j = [0,1]
k = [0,1,2]

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + k != number:
#                 combinatinos.append([i,j,k])

# print(combinatinos)

a= [ [i,j,k] for i in range(x+1) for j in range(y+1)  for k in range(z+1) if i + j + k != number]

print(a)