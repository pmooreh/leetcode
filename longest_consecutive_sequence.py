
class Ranger:
  def __init__(self):
    self.interval_starts = dict()
    self.interval_ends = dict()
    self.seen = set()
  def add(self, num):
    if num in self.seen:
      return
    n_prev, n_next = num - 1, num + 1
    if n_prev not in self.interval_ends and n_next not in self.interval_starts:
      self.interval_starts[num] = num
      self.interval_ends[num] = num
      self.seen.add(num)
      return
    if n_prev in self.interval_ends:
      interval_start = self.interval_ends[n_prev]
      del self.interval_ends[n_prev]
      self.interval_ends[num] = interval_start
      self.interval_starts[interval_start] = num
    if n_next in self.interval_starts:
      interval_end = self.interval_starts[n_next]
      del self.interval_starts[n_next]
      self.interval_starts[num] = interval_end
      self.interval_ends[interval_end] = num
    if num in self.interval_starts and num in self.interval_ends:
      start = self.interval_ends[num]
      end = self.interval_starts[num]
      del self.interval_starts[num]
      del self.interval_ends[num]
      self.interval_starts[start] = end
      self.interval_ends[end] = start
    self.seen.add(num)
  def get_intervals(self):
    intervals = []
    for start in self.interval_starts:
      intervals.append((start, self.interval_starts[start]))
    return intervals

def lcs(nums):
  r = Ranger()
  for n in nums:
    r.add(n)
  return max(interval[1] - interval[0] + 1 for interval in r.get_intervals())

if __name__ == '__main__':
  assert lcs([100, 4, 200, 1, 3, 2]) == 4

