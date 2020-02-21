import math

def interchange(a, x, y):
    '''
    This method interchanges the elements at index x and y in the list a
    input : list, index1, index2
    '''
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

def firstAsPivot(a, f, l):
    '''
    this method sets first element of a given unsorted list as the pivot element
    input : the entire list, starting index of the sub list, last index of the sub list
    output : element at the startinng index of the sub list
    '''
    return a[f]

def lastAsPivot(a, f, l):
    '''
    this method sets last element of a given unsorted list as the pivot element
    input : the entire list, starting index of the sub list, last index of the sub list
    output : element at the last index of the sub list
    '''
    return a[l]


# set median of the first, last and the middle element of unsorted list at pivot
def medianAsPivot(a, f, l):
    '''
    this method sets the median of the first, last and the middle element of unsorted list at pivot
    input : the entire list, starting index of the sub list, last index of the sub list
    output : element at the last index of the sub list
    '''
    length = l-f+1
    tempArray = [a[l], a[f]]
    m = math.floor((l+f)/2)
    tempArray.append(a[m])
    tempArray.sort()
    return tempArray[1]


# subroutine to partition the list around the chosen pivot
def Partition(a, f, l, pivot):
    '''
    this method partitions the sublist around the chosen pivot and returns the new position of the pivot after partition
    input : the entire list, starting index of the sub list, last index of the sub list, pivot element
    output : position of the pivot after partition
    '''
    interchange(a, f, a.index(pivot))
    i = f+1
    for j in range(f+1, l+1):
        if a[j] < pivot:
            interchange(a, i, j)
            i += 1
    interchange(a, f, i-1)
    return i-1


# the quicksort subroutine
def QuickSort(a, f, l):
    '''
    This is our main method that computes the entire quicksort algorithm
    input : the entire list, starting index of the sub list, last index of the sub list
    '''
    global comparisons
    if f<l:
        comparisons += l-f   #kepping track of comparisons
        # pivot = firstAsPivot(a, f, l)
        # pivot = lastAsPivot(a, f, l)
        pivot = medianAsPivot(a, f, l)
        partitionIndex = Partition(a, f, l, pivot)
        QuickSort(a, f, partitionIndex-1)
        QuickSort(a, partitionIndex+1, l)



# reading the file and loading the values in a list
intFile = open('QuickSort.txt','r')
intlist=[]
for line in intFile.readlines():
    intlist.append(int(line))
intFile.close()
print("The length of the given list is {}".format(len(intlist)))
print("The list before sorting is as follows:")
print(intlist[0:])
comparisons = 0  #initialize the comparison counter
QuickSort(intlist, 0, len(intlist)-1)  #outermost call to quicksort subroutine
print("\nThe list after sorting is as follows:")
print(intlist[0:])
print("\nThe total numbetr of comparisons required are:",comparisons)

