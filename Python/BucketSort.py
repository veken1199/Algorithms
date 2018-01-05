# This algorithm only supports array of positive numbers
import QuickSort as qs

def BucketSort(arr, buckets_num=10):
      output = []

      # Create 10 buckets or any number specified
      buckets = [[] for x in range(buckets_num)]

      # separate the numbers into buckets
      # each bucket will contain a specific range of numbers depending on both buckets_num
      # and the max num in the passed arr
      print(max(arr))
      for i in range(len(arr)):
            buckets[int(arr[i]/(max(arr)*buckets_num))].append(arr[i])
      
      # sort each bucket separately
      for bucket in buckets:
            output += qs.QuickSortRecurrsive(bucket)
      return output

print(BucketSort([1,3,3,2,1,123,412,1,4,123,123,5,124,12,123,12331]))