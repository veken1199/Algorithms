def selectionSort(arr):
      output_arr = []

      while(len(arr) != 0):
            
            min_index = 0  
            count = 0

            for i in range(count, len(arr)):
                  # First : find the min number in the list
                  if( arr[i] < arr[min_index] ):
                        min_index = i

            # Second: add the min to a new list
            output_arr.append(arr[min_index]) 

            # Third: remove the the smallest number from the list
            arr.pop(min_index)
      return output_arr

            

def selectionSortInPlace(arr):
      start = 0
      min_index = start

      while(start != len(arr)):
            for end in range (start,len(arr)):
                  if(arr[min_index] > arr [end]):
                        min_index = end

            arr[start],arr[min_index] = arr[min_index], arr[start]
            start+=1
            min_index = start
      return arr
             
print(selectionSort([2,3,1,9,6,4,2,3,1,55,2,33,4,12,-1,2,-120,3]))
print(selectionSortInPlace([2,3,1,9,6,4,2,3,1,55,2,33,4,12,-1,2,-120,3]))