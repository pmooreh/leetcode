
def index_prev_chars(s):
  prevs = {chr(i): -1 for i in range(ord('a'), ord('z') +1)}
  ret = []
  for i, c in enumerate(s):
    ret.append(prevs.copy())
    prevs[c] = i
  return ret

def lps(s, prev_idxs, start, end):
  if start >= end:
    return ''
  curr_char = s[start]

  lps_take = curr_char
  next_char_idx_from_end = end-1 if s[end-1] == curr_char else prev_idxs[end-1][curr_char]
  if next_char_idx_from_end > start:
    lps_take += lps(s, prev_idxs, start+1, next_char_idx_from_end) + curr_char

  lps_skip = lps(s, prev_idxs, start+1, end)

  return lps_take if len(lps_take) > len(lps_skip) else lps_skip

def longest_palindromic_subseq(s):
  return lps(s, index_prev_chars(s), 0, len(s))




def check_is_palindrome(s, pals, start, end):
  if end - start <= 1 or (s[start] == s[end - 1] and (start+1, end-1) in pals):
    pals.add((start, end))

def lpss(s):
  if not s:
    return ''
  pals = set()
  for l in range(len(s) + 1):
    for i in range(len(s) - l + 1):
      check_is_palindrome(s, pals, i, i+l)
  lpb = max(pals, key=(lambda e: e[1] - e[0]))
  return s[lpb[0]:lpb[1]]


