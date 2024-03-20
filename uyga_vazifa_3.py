class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = set(nums2)
        nums4 = set(nums1)
        answer = []
        count = 0
        count1 = 0
        for i in nums1:
            if i in nums3:
                count += 1
        answer.append(count)

        for j in nums2:
            if j in nums4:
                count1 += 1
        answer.append(count1)
        return answer



