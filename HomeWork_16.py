def sorter(list):
    for srt in range(len(list)-1):
        for i in range(len(list)-1-srt):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list
list=[5,85,3,5,78,4,6,35,0]
sorter(list)
print(list)