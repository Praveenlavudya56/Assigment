import heapq

# Create an empty list to use as a heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)

print("Min heap:", heap)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)
print("Remaining heap:", heap)

# Get the smallest element without removing it
smallest = heap[0]
print("Smallest element:", smallest)

# Convert a list to a heap in linear time
arr = [5, 3, 8, 1, 10]
heapq.heapify(arr)
print("Heapified array:", arr)
