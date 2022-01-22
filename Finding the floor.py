import sys
class Solution:
    def floor(self,arr,k):
        n=len(arr)
        ans=-sys.maxsize-1
        for i in range(n):
            if arr[i]<=k and arr[i]>ans:
                ans=arr[i]
        return ans

    def Floorsearch(self,a, n, k):
        a.sort()
        ans=-2147483648
        l, h = 0, n - 1
        while (l <= h):
            mid = (l + h) // 2
            if a[mid] <=k:
                ans=arr[mid]
                l = mid + 1
            elif a[mid] > k:
                h = mid - 1

        return ans




if __name__=="__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        k=int(input())
        obj=Solution()
        print(obj.Floorsearch(arr,len(arr),k))
