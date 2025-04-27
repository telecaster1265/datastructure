import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)
    

if __name__ == '__main__':
    print("힙 정렬을 수횅합니다.")
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
    
    heap_sort(x)  
    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")