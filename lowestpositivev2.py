arr = [ -1, 1, 2 , 3,7]
sorted_arr = [ i for i in sorted(arr) if i > 0 ]

result = sorted_arr[-1] + 1
for i in range(len(sorted_arr)):
    if i > len(sorted_arr):
        if sorted_arr[i+1] - sorted_arr[i] > 1:
            result = sorted_arr[i] + 1
            break
print(result)