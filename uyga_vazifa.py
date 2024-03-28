#2103-leetcode issues
class Solution:
    def countPoints(self, rings: str) -> int:
        r, g, b = set(), set(), set()
        for index in range(0,len(rings),2):
            if rings[index] == "R":
                r.add(rings[index+1])
            elif rings[index] == "G":
                g.add(rings[index+1])
            else:
                b.add(rings[index+1])
        return len(r&g&b)

#2108-leetcode issues
class Solution:
    def ispalindrome(self, word: str) -> bool:
        if word == word[::-1]:
            return word

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.ispalindrome(word):
                return word
        return ""
#2114-leetcode issues
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for i in sentences:
            a = i.split(" ")
            arr.append(len(a))
        return max(arr)