#Build min heap 
#(Time complexity : O(n) and Space : O(1))
A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A)
print(A)

# Inset a element to heap usonh heappush
#Time O(logn)
heapq.heappush(A,4)
print(A)

# delete a element to heap usonh heappush
#Time O(logn)
min = heapq.heappop(A)
print(A,min)

#Peak the min elements from heap 
#Time Compleity : O(1)
A[0]
print(A[0])

#Heap Sort 
#Time : O(nlogn) , Space : O(n)
# NOte : O(1) is possible using swaping but this is complex 

def heapsort(arr):
    new_list=[0] * len(arr)
    heapq.heapify(arr)

    for i in range(len(arr)):
       min=  heapq.heappop(arr)
       new_list[i]= min
    print(new_list)

    return new_list
heapsort([1,3,5,7,9,2,4,6,8,0])

#Heap Push Pop: Time: O(logn)
heapq.heappushpop(A,99)
print(A)


#Build max heap 

B = [-4,3,1,0,2,5,10,8,12,9]

heapq.heapify(B)
print(B)

for i in range(len(B)):
    B[i] = -B[i]
heapq.heapify(B)
print(B)

largest = -heapq.heappop(B)
print(largest)


#Build from scratch 
#Time Complexity : O(nlogn)
C =[-5,4,2,1,7,0,3]
heap=[]

for x in C:
    heapq.heappush(heap,x)
    print(heap)

#Putting Tuple on the heap 
D = [5,4,3,5,4,3,5,5,4]
from collections import Counter 

counter = Counter(D)
print(counter)

heap=[]

for k,v in counter.items():
    heapq.heappush(heap,(k,v))
print(heap)


