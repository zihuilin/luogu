lst = [-21,-3,0,3,6,9,10,100]
lst = [-21,-3,0,0,3,6,9,10,100]
lst = [0,0,3,6,9,10,100]
lst = [-21,-3,0,0,0,0]
lst = [0,0,0,0,0]

def binary_right_serach(lst, target):
    if len(lst) == 0:
        return -1

    left = 0
    right = len(lst) - 1

    while left + 1 < right:  #当搜索区域多于2个元素
        mid = (left + right) // 2
        if lst[mid] == target : 
            left = mid
        elif lst[mid] > target:
            right = mid
        elif lst[mid] < target:
            left = mid

    if lst[right] == target:
        return right
    elif lst[left] == target:
        return left
    else:
        return -1

i = binary_left_serach(lst, 0) #在lst里搜索元素为0的下标
print(i)

