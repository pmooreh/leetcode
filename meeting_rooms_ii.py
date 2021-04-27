from queue import PriorityQueue

def min_meeting_rooms(intervals):
  intervals = sorted(intervals, key=(lambda elem: elem[0]))
  roomQueue = PriorityQueue()
  max_rooms = 0
  for interval in intervals:
    start, end = interval
    earliest_end_time = None
    while not roomQueue.empty():
      earliest_end_time = roomQueue.get(block=False)
      if earliest_end_time > start:
        break
    if earliest_end_time is not None and earliest_end_time > start:
      roomQueue.put(earliest_end_time)
    roomQueue.put(end)
    max_rooms = max(roomQueue.qsize(), max_rooms)
  return max_rooms

if __name__ == '__main__':
  assert min_meeting_rooms([[1,5], [6,10]]) == 1
  assert min_meeting_rooms([[1,5], [4,10]]) == 2
  assert min_meeting_rooms([[0, 30],[5, 10],[15, 20]]) == 2
  assert min_meeting_rooms([[7,10],[2,4]]) == 1
  assert min_meeting_rooms([]) == 0

