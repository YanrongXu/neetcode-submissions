class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length - 1):
            maxNum = max(arr[i + 1:])
            arr[i] = maxNum
        arr[length - 1] = -1
        return arr