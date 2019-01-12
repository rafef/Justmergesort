def mergeSort(List):
    left = []
    right = []
    middle = len(List)/2
    for i in range(0,middle):
        left.append(List[i])
    for i in range(middle, len(List)):
        right.append(List[i])
    print(left)
    print(right)
    return(merge(left,right))
def merge(left,right):
    answer = []
    leftholder = 0
    rightholder = 0
    i = 0
    while leftholder < len(left) and rightholder < len(right):
        if left[leftholder] <= right[rightholder]:
            answer.append(left[leftholder])
            leftholder += 1
        else:
            answer.append(right[rightholder])
            rightholder += 1
    print(answer)
    return answer
h = (6, 9 , 4, 2, 1, 5, 6, 9)
h = mergeSort(h)
h = mergeSort(h)
