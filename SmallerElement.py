class Solution:
    def smallerele(self,arr): #Brute Force using a count array 0(n^2
        n=len(arr)
        count=[0]*n
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    count[i]+=1
        return sum(count)

    def smallerele2(self,arr): #using mergesort 0(nlogn+n)
        ans = [0]*len(arr)
        ar = [[v, i] for i, v in enumerate(arr)]
        self.merge_sort(ar, ans)
        return sum(ans)

    def merge_sort(self, arr=[], ans=[]):
        if len(arr) <= 1:
            return

        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        self.merge_sort(left_array, ans)
        self.merge_sort(right_array, ans)
        self.merge(left_array, right_array, arr, ans)

    def merge(self, left_array, right_array, array, ans):
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):

            if left_array[i][0] <= right_array[j][0]:

                array[k] = left_array[i]
                ans[left_array[i][1]] += k - i
                i += 1
            else:

                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):

            array[k] = left_array[i]
            # Step 4
            ans[left_array[i][1]] += k - i
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1



if __name__=="__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        obj=Solution()
        print(obj.smallerele2(arr))
