import heapq
def heapify(lst):
    heap = lst[:]
    heapq.heapify(heap)
    return heap
def heapsort(lst):
    return heapify(lst), [heapq.heappop(lst) for _ in range(len(lst))]
# 测试代码
data = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
sorted_data, sorted_output = heapsort(data)
print('Heap after heapify:', sorted_data) # 堆后 heapify 后的堆输出为：[2, 1, 3, 5, 4, 6]
print('Sorted output:', sorted_output) # 排序结果输出为：[1, 2, 3, 4, 5, 6]