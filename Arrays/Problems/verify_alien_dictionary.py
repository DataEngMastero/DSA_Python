class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderedIndex = { c: i for i, c in enumerate(order) }

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if orderedIndex[c2] < orderedIndex[c1]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True
