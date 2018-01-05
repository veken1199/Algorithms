def BubbleSort(arr):
      dirty = True
      
      while(dirty):
            dirty = False
            for i in range(len(arr)-1):
                  if(arr[i] > arr[i+1]):
                        arr[i],arr[i+1] = arr[i+1], arr[i]
                        dirty = True

      return arr

def main():
      print(BubbleSort([2,3,1,9,6,4,2,3,1,55,2,33,4,12,-1,2,-120,3]))

