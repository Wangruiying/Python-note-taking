def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
            print ("if----",index)
        i+=1
    print ("while----",index)
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if "__main__" == __name__:
    '''
    test = input("数组:") # //输入一个一维数组，每个数之间使用 ，隔开
    num = [int(n) for n in test.split(",")]
    #test = [1,3,6,8,9,5]
    print (num)
    #test =[]
    print (quickSort(num))
   ''' 
    list = input("数组：").split(",")
    print (quickSort(list))

