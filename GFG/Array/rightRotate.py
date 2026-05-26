class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        k = d % n

        # Reverse whole array
        l, r = 0, n - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # Reverse first k
        l, r = 0, k - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # Reverse remaining
        l, r = k, n - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        return arr