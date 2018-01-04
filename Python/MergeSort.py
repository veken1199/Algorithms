def MergeSort(arr):
      output = []

      if len(arr)<=1:
            return arr

      else:
            arr1,arr2 = partition(arr)
            arr1 = (MergeSort(arr1))
            arr2 = (MergeSort(arr2))

            # Merging the sorted parts into one list
            while(arr1 and arr2):
                  if arr1[0] <= arr2[0]:
                        output.append(arr1[0])
                        arr1.pop(0)
                  else:
                        output.append(arr2[0])
                        arr2.pop(0)

            output += arr1 + arr2
            return output

def partition(arr):
      return arr[0:int(len(arr)/2)], arr[int(len(arr)/2):len(arr)]

print(partition([1,2,3,4]))
print(MergeSort([1,4,23,3,4,7,8,5,3,4,1,12]))