Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?  
   Runtime doesn't grow relative to the input so it's Constant time:  
   O(1)

2. What is the space complexity of your ring buffer's `append` function?  
   O(1)

3. What is the runtime complexity of your ring buffer's `get` method?  
   Worst case is that it performs an operation for every item in the storage list, so it is Linear time:  
   O(n)

4. What is the space complexity of your ring buffer's `get` method?  
   O(n)

5. What is the runtime complexity of the provided code in `names.py`?  
   A for loop nested in a for loop makes it quadratic time:  
   O(n^2)

6. What is the space complexity of the provided code in `names.py`?  
   It stores one potential duplicate for each input (worst case every name is a duplicate), so it is:  
   O(n)

7. What is the runtime complexity of your optimized code in `names.py`?  
    Contains method is O(log(n) and it is within a for loop so the overall time complexity is Log Linear time:
   O(n log(n))

8. What is the space complexity of your optimized code in `names.py`?  
   O(n)
