
def binarySearch(array,k):
    start=0
    end=len(array)-1
    while(start<=end):
        mid=start+(end-start)//2
        if(array[mid]==k):
            return mid
        elif(array[mid]>k):
            end=mid-1
        else:
            start=mid+1
    return -1

def findX(array,x):
    index=binarySearch(array,x)
    if(index!=-1):
        start=index-1
        while(start>=0 and array[start]==k):
            start-=1
        start+=1
        end=index+1
        while(end<len(array) and array[end]==k ):
            end+=1
        end-=1
        print('{} {}'.format(start,end))
    else:
        print("-1")
            


t= int(input())
while(t):
    t-=1
    n,k=[int(x) for x in input().split()]
    array=[int(x) for x in input().split()]
    findX(array,k)
    
