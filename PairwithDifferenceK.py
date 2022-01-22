import sys
'''Kishan Mishra'''
class Solution :
    #Brute Force
    def sumofpairs(self,arr,k):  #O(N^2)
        n=len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]-arr[j]==k:
                    return True
                return False

    #Two-pointer Method
    def sumofpairs2(self,arr,k): #0(NLOGN+N)
        arr.sort() #timsort in python uses merge sort so time complexity is nlogn
        n=len(arr)
        sum=0
        bool=False
        l=0
        h=n-1
        while(l<h):
            diff=arr[l]-arr[h]
            if sum>k:
                h-=1
            elif sum<k:
                l+=1
            else:
                bool=True
                break
        return bool

    #Binary-search Method
    def binarysearch(self,a,l,h, k): #O(nlogn(sorting))+0(nlogn)Binay search
        pos = 0
        while (l <= h):
            mid = (l + h) // 2
            if a[mid] < k:
                l = mid + 1
            elif a[mid] > k:
                h = mid - 1
            elif a[mid] == k:
                pos = mid
                return True
        return False

    def sumofpairs3(self,arr,k):
        arr.sort()
        n=len(arr)
        for i in range(n):
            b=k+arr[i]
            if (self.binarysearch(arr,0,n-1,b)):
                return True
        return False


if __name__=="__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        obj=Solution()
        if (obj.sumofpairs3(arr, k)):
            print("true")
        else:
            print("false")
