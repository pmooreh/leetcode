import heapq

def skyline(buildings):
  if len(buildings) == 0:
    return []
  buildings = sorted(buildings, key=(lambda b: b[0]))
  y_bound = max(b[2] for b in buildings)
  max_heights = [[0, 0, y_bound]]
  leading_vertices = []
  up_to = 0
  for building in buildings:
    curr_a, curr_b, curr_h = building
    top_h, top_a, top_b = heapq.heappop(max_heights)
    top_h *= -1
    while top_b < curr_a:
      if top_b > up_to:
        leading_vertices.append([max(up_to, top_a), top_h])
        up_to = top_b
      top_h, top_a, top_b = heapq.heappop(max_heights)
      top_h *= -1
    if top_h > curr_h and top_b >= curr_b:
      heapq.heappush(max_heights, [-top_h, top_a, top_b])
    elif top_h > curr_h and top_b < curr_b:
      heapq.heappush(max_heights, [-top_h, top_a, top_b])
      heapq.heappush(max_heights, [-curr_h, top_b, curr_b])
    elif top_h < curr_h and top_b > curr_b:
      leading_vertices.append([top_a, top_h])
      up_to = curr_a
      heapq.heappush(max_heights, [-curr_h, curr_a, curr_b])
      heapq.heappush(max_heights, [-top_h, curr_b, top_b])
    elif top_h < curr_h and top_b <= curr_b:
      leading_vertices.append([top_a, top_h])
      up_to = curr_a
      heapq.heappush(max_heights, [-curr_h, curr_a, curr_b])
  return leading_vertices

