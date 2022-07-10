from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for j in range(len(pattern)):
      char = pattern[j]
      table[char] = j

    return table

class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, bad_char: str, j: int) -> int:
        assert len(bad_char) == 1

        if bad_char in self.table:
            b = self.table[bad_char]
        else:
            b = -1
        return max(j-b, 1)

    def search(self) -> int:
        len_text = len(self.text)
        len_pattern = len(self.pattern)
        m = len(self.pattern)
        n = len(self.text)

        s = 0
        while(s <= len_text-len_pattern):
          j = len_pattern-1
          
          while j>=0 and self.pattern[j] == self.text[s+j]:
            j = j-1

          if j<0:
            return s

          else:
            s += self.decide_slide_width(self.text[s+j], j)

        return -1

if __name__ == '__main__':
    pattern = 'GCTCG'
    text = 'GCTCACTGAGCGCTCGT'
    b = Bm(text, pattern)
    print(b.search())
	
