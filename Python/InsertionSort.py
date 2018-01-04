def InsertionSort(arr):
      for i in range(len(arr)):
            pointer = i
            while(pointer != 0):
                  if (arr[pointer] < arr[pointer-1]):
                        arr[pointer],arr[pointer-1] = arr[pointer-1], arr[pointer]
                        pointer-=1
                  else:
                        break
      return arr

print(InsertionSort([2,3,1,9,6,4,2,3,1,55,2,33,4,12,-1,2,-120,3]))