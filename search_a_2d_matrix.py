def search(matrix, target):
  if all(len(col) == 0 for col in matrix):
    return False
  tgt_row = bisect.bisect([r[0] for r in matrix], target) - 1
  if not 0 <= tgt_row < len(matrix):
    return False
  tgt_col = bisect.bisect_left(matrix[tgt_row], target)
  return  0 <= tgt_col <= len(matrix[tgt_row]) and matrix[tgt_row][tgt_col] == target
