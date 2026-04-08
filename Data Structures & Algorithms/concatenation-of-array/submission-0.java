class Solution {
    public int[] getConcatenation(int[] nums) {
   

   int capcity = 2;
   int[] newArray = new int[nums.length * capcity];
  for(int i = 0; i<nums.length; i++){
  newArray[i] = nums[i];
   newArray[i + nums.length] = nums[i];
  }

return newArray;

    }
   

  
}