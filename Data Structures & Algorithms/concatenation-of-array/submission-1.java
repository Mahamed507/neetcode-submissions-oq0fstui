class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] newA = new int[nums.length * 2];

        for(int i = 0; i<nums.length; i++){
            newA[i]=nums[i];
            
           newA[i+nums.length] = nums[i];
           

        } return newA;
    }
}