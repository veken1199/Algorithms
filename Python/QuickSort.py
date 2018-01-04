def QuickSortRecurrsive(arr):
      if(len(arr) <= 1):
            return arr
      else:
            # Pick the pivot and get the parts
            arr1,arr2 = partition(arr, len(arr)-1)
            return QuickSortRecurrsive(arr1) + [arr[len(arr)-1]] + QuickSortRecurrsive(arr2)

            
def partition(arr, pivot_index):
      arr1 = []
      arr2 = []

      # Put the smaller values than the pivot in arr1, 
      # Put the bigger values than the pivot in arr2
      for i in (x for x in range(len(arr)) if x!= pivot_index):
            
            if(arr[i] > arr[pivot_index]):
                  arr2.append(arr[i]) 
            else: arr1.append(arr[i])
      
      return arr1, arr2


print (QuickSortRecurrsive([1,4,3,2,1,-12,23,2132,4,2,-12,2,-2,-3,33,2,21]))