#Implementation of Bubble sort algorithm in Python
#@author Mark kihara

list_A=[8,5,4,2,6,8]

def Bubble_sort():
    indexing_length=len(list_A)-1
    sorted=False

    while not sorted:
        sorted=True

        for i in range(indexing_length):

            if (list_A[i]>list_A[i+1]):
                sorted=False
                list_A[i], list_A[i+1]=list_A[i+1],list_A[i]
    return list_A

print(Bubble_sort(list_A))