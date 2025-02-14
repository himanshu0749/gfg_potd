Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.

Examples:

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base is 2. Height of container = min(5, 3) = 3. So, total area to hold water = 3 * 2 = 6.




------------------------------------------------------------------------------------------------------------------------------------------------------
In java
{
  class Solution {

    public int maxWater(int arr[]) {
        // Code Here
        int i = 0 , j = arr.length-1 , ar = 0;
        while( i < j){
            int h = Math.min( arr[i] , arr[j]);
            int w = j - i;
            ar = Math.max(ar , h*w);
            
            if( arr[i] < arr[j]){
                i++;
            }else{
                j--;
            }
        }
        return ar;
        
        
    }
}
}



In Python

class Solution:
    def maxWater(self, arr):
        # code here
        i , j , area = 0 , len(arr)-1 , 0
        while i < j :
            h = min(arr[i] , arr[j])
            w = j - i
            area = max(area , h*w)
            
            if arr[i] < arr[j]:
                i+=1
            else:
                j-=1
        return area
