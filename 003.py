# 3. Find the Maximum Number in a List
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([4, 1, 9, 7]))  # Output: 9


def fmax(lst):
    mx = lst[0]

    for i in lst:
        if i>mx:
            mx=i

    return mx

print(fmax([1,4,7,3,7,8,44,87,34])) #87
    
        