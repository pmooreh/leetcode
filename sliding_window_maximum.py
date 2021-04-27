import heapq
from collections import deque

def max_in_window(heap, start_index, window_size):
  top = heap[0]
  while not (start_index <= top[1] < start_index + window_size):
    heapq.heappop(heap)
    top = heap[0]
  return -1 * top[0]

def max_sliding_window(nums, k):
  if nums == []:
    return []
  inverted_elems = [(-n, i) for i, n in enumerate(nums)]
  inverted_heap = inverted_elems[:k]
  heapq.heapify(inverted_heap)
  maxs = []
  for w in range(len(nums) - k):
    maxs.append(max_in_window(inverted_heap, w, k))
    heapq.heappush(inverted_heap, inverted_elems[w + k])
  maxs.append(max_in_window(inverted_heap, len(nums) - k, k))
  return maxs


def msw_deque(nums, k):
  window = deque()
  maxs = []
  for idx, val in enumerate(nums):
    while window and window[0] <= idx - k:
      window.popleft()
    while window and nums[window[-1]] < val:
      window.pop()
    window.append(idx)
    if idx >= k - 1:
      maxs.append(nums[window[0]])
  return maxs
    

