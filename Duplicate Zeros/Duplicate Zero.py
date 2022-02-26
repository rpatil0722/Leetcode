class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr1=[]
        l=len(arr)
        i=0
        j=0
        for i in range(0,l):
                if(arr[i]==0):
                    arr1.append(arr[i])
                    arr1.append(arr[i])
                    i+=1
                    j+=2
                    
                else:
                    arr1.append(arr[i])
                    i+=1
                    j+=1
        for x in range(0,len(arr)):
            arr[x]=arr1[x]
        