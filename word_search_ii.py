
class TrieNode:
  def __init__(self, c):
    self.nexts = {}
    self.c  = c
    self.word = False
  def add(self, up_to, remaining):
    if not remaining:
      self.word = up_to
      # print(up_to)
      return
    if remaining[0] not in self.nexts:
      self.nexts[remaining[0]] = TrieNode(remaining[0])
    self.nexts[remaining[0]].add(up_to + remaining[0], remaining[1:])
  def __repr__(self):
    return '{}: {} => {}'.format(self.word, self.c, self.nexts.keys())


class Trie:
  def __init__(self):
    self.root = TrieNode('')
  def add(self, word):
    self.root.add('', word)

def search_for_words(board, words):
  trie = Trie()
  for word in words:
    trie.add(word)
  all_coords = []
  for r in range(len(board)):
    for c in range(len(board[r])):
      all_coords.append((r, c))
  found = set()
  for starting_coord in all_coords:
    # print('-- {} --'.format(starting_coord))
    currents = []
    nexts = []
    starting_char = board[starting_coord[0]][starting_coord[1]]
    if starting_char in trie.root.nexts:
      currents.append((starting_coord, trie.root.nexts[starting_char], set()))
    while currents:
      for current_coord, current_node, current_seen in currents:
        if current_coord in current_seen or not current_node:
          continue
        # print(current_coord)
        # print(current_node)
        if current_node.word:
          found.add(current_node.word)
        next_seen = set(current_seen)
        next_seen.add(current_coord)
        r, c = current_coord
        deltas = [(-1, 0) , (1, 0) , (0, -1), (0, 1)]
        for r_delta, c_delta in deltas:
          next_r, next_c = r + r_delta, c + c_delta
          if 0 <= next_r < len(board) and 0 <= next_c < len(board[next_r]):
            next_char = board[next_r][next_c]
            if next_char in current_node.nexts:
              nexts.append(((next_r, next_c), current_node.nexts[next_char], next_seen))
      currents = nexts
      nexts = []
  # print(found)
  return found

if __name__ == '__main__':
  board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
  ]
  words = ["oath","pea","eat","rain"]
  assert search_for_words(board, words) == set(["eat","oath"])

  board = [["a","b"],["a","a"]]
  words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
  assert search_for_words(board, words) == set(["aaa","aaab","aaba","aba","baa"])
