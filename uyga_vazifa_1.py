class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        str1 = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                str1.append(i)
        return str1
