

def binarySearchModified(arr):

    start=0
    end=len(arr)-1
    n=len(arr)
    mid=0
    while(start<=end):
        mid=start+(end-start)//2
        pre= mid-1 if mid>0 else n-1
        print('start: {}, end: {}, mid{}'.format(start,end,mid))
        if((arr[mid]>arr[(mid+1)%n]) and arr[mid]>arr[pre]):
            print('returning')
            return arr[mid]
        if(arr[mid]>arr[start]):
            start=mid+1
        else:
            end=mid-1

    return arr[mid]
t=int(input())
while(t):
    t-=1
    n=int(input())
    print(n)
    arr=[int(x) for x in raw_input().split(" ")]
    print(binarySearchModified(arr))
    
        
