def split_range(interval, n_splits):
  start, end = interval
  length = end - start
  split_lengths = length // n_splits
  remainder_length = length % n_splits
  ranges = []
  for n_split in range(n_splits):
    split_start = start if not ranges else ranges[-1][1]
    split_end = split_start + split_lengths + (1 if n_split < remainder_length else 0)
    if split_end - split_start == 0:
      break
    ranges.append((split_start, split_end))
  return ranges

def split_into_quadrants(bounding_box):
  '''quadrant is specified as top_left, bottom_right'''
  quadrants = []
  row_range = (bounding_box[0][0], bounding_box[1][0])
  col_range = (bounding_box[0][1], bounding_box[1][1])
  for row_split in split_range(row_range, 2):
    for col_split in split_range(col_range, 2):
      top_left = (row_split[0], col_split[0])
      bottom_right = (row_split[1], col_split[1])
      quadrants.append((top_left, bottom_right))
  return quadrants

def search_within_bounding_box(matrix, bounding_box, target):
  top_left_val = matrix[bounding_box[0][0]][bounding_box[0][1]]
  bottom_right_val = matrix[bounding_box[1][0]-1][bounding_box[1][1]-1]
  if top_left_val == target or bottom_right_val == target:
    return True
  if target > bottom_right_val or target < top_left_val:
    return False
  quadrants_to_search = split_into_quadrants(bounding_box)
  # print(quadrants_to_search)
  for quadrant in quadrants_to_search:
    if search_within_bounding_box(matrix, quadrant, target):
      return True
  return False

def search_matrix(matrix, target):
  initial_bounding_box = ( (0,0), (len(matrix),len(matrix[0])) )
  return search_within_bounding_box(matrix, initial_bounding_box, target)


if __name__ == '__main__':
  matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
  ]
  assert search_matrix(matrix, 5) == True
  assert search_matrix(matrix, 20) == False

