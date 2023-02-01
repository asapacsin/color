import numpy as np
import copy

def get_index(index,size=4):
    if index < 0:
        index = size +index
    elif index >= size:
        index = index -size
    return index

def judge_right(arr,size,index,cur_color):
    pre_index = get_index(index-1,size)
    next_index = get_index(index+1,size)
    pre_color = arr[pre_index]
    next_color = arr[next_index]
    pre_judge = False
    next_judge = False
    if pre_color == 0:
        pre_judge = True
    else:
        if pre_color != cur_color:
            pre_judge = True
    if next_color == 0:
        next_judge = True
        if next_color != cur_color:
            next_judge = True
    judge = pre_judge and next_judge
    return judge

def index_ful(arr,size,index,color):
    if index >= size:
        return 1
    if color > size:
        return 0
    if judge_right(arr,size,index,color) == False:
        return 0
    get_arr = copy.deepcopy(arr)
    get_arr[index] = color
    index_color = 1
    return index_ful(arr,size,index+1,index_color)+color_ful(arr,size,index,color+1)

def color_ful(arr,size,index,color):
    if color > size:
        return 0
    if judge_right(arr,size,index,color) == False:
        return 0
    get_arr = copy.deepcopy(arr)
    get_arr[index] = color
    index_color = 1
    return index_ful(arr,size,index+1,index_color)+color_ful(arr,size,index,color+1)
        


a = np.zeros(4)
for i in range(1,5,1):
    a[i] = 