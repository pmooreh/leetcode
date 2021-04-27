from bisect import bisect_left

def median_in_l1(l1, l2, interval):
  start, end = interval
  if start == end:
    return None
  midpoint = (end - start) // 2 + start
  pos_in_l2 = bisect_left(l2, l1[midpoint])
  n_left = midpoint + pos_in_l2
  n_right = len(l1) + len(l2) - (midpoint+1) - (pos_in_l2)
  if abs(n_left - n_right) <= 1:
    return midpoint
  if n_left < n_right:
    return median_in_l1(l1, l2, (midpoint+1, end))
  else:
    return median_in_l1(l1, l2, (start, midpoint))

def get_meds(nums1, nums2):
  m_l1 = median_in_l1(nums1, nums2, (0, len(nums1)))
  m_l2 = median_in_l1(nums2, nums1, (0, len(nums2)))
  return m_l1, m_l2
'''
def find_median(nums1, nums2):
  m_l1 = median_in_l1(nums1, nums2, (0, len(nums1)))
  m_l2 = median_in_l1(nums2, nums1, (0, len(nums2)))
  if (len(nums1) + len(nums2)) % 2 == 0:
    if m_l1 is not None and m_l2 is not None:
      return (nums1[m_l1] + nums2[m_l2]) / 2
    if m_l1 is not None:

      return (nums1[m_l1] + nums2[m_l2]) / 2
    if m_l1 is not None and m_l2 is not None:
      return (nums1[m_l1] + nums2[m_l2]) / 2


  return m_l1, m_l2
'''